import config
import datetime
import apps.config
from flask import Blueprint, render_template, request, session
from .forms import (
    TakeComm,
)
from apps.mc.models import MCUser
from ..models import PosViewModel
from flask_paginate import Pagination, get_page_parameter
from .models import CommModel, CommLineModel, BrokerModel, CommBrokerModel
from apps.decorators import login_required
from sqlalchemy import func
from exts import db
from utils import restful

bp = Blueprint("broker", __name__, url_prefix='/broker')


@bp.route('/')
@login_required
def show_comm():
    pending = db.session.query(PosViewModel).filter(PosViewModel.sale_line_id.notin_(CommLineModel.sale_line_id))

    result = db.session.query(
        pending.order_num,
        pending.group_name,
        pending.car,
        pending.order_date,
        func.sum(pending.amt).label('subtotal')
    ).filter(pending.sale_line_id.isnot(None)) \
        .group_by(pending.order_num,
                  pending.group_name,
                  pending.car,
                  pending.order_date) \
        .all()

    brokers = BrokerModel.query.order_by(BrokerModel.broker_id)

    context = {
        'rewords': result,
        'brokers': brokers
    }

    return render_template('broker/broker.html', **context)


@bp.route('/distribute/', methods=['POST'])
@login_required
def distribute():
    pending = db.session.query(PosViewModel).filter(PosViewModel.sale_line_id.notin_(CommLineModel.sale_line_id))
    form = TakeComm(request.form)
    if form.validate():
        order_num = form.order_num.data
        group_name = form.group_name.data
        car = form.car.data
        order_date = form.order_date.data
        broker_id = form.broker_id.date

        result = db.session.query(
            pending.order_num,
            pending.group_name,
            pending.car,
            pending.order_date,
            func.sum(pending.amt).label('subtotal')
        ).filter(
            order_num == pending.order_num,
            group_name == pending.group_name,
            car == pending.car,
            order_date == pending.order_date
        ).group_by(
            pending.order_num,
            pending.group_name,
            pending.car,
            pending.order_date).all()
        user_id = session.get(config.MC_USER_ID)
        user = MCUser.query.filter_by(user_id=user_id).first()
        for row in result:
            comm = CommModel(order_num=row.order_num,
                             group_name=row.group_name,
                             car=row.car,
                             order_date=row.order_date,
                             sale_amt=row.subtotal,
                             rate=apps.config.COMM_RATE,
                             comm_amt=apps.config.COMM_RATE*row.subtotal+apps.config.GUARANTEE_FEE,
                             comm_type='銷售佣金',
                             cal_type='自動',
                             status='NEW',
                             created_at=datetime.now(),
                             created_by=user.account,
                             updated_at=datetime.now(),
                             updated_by=user.account
                             )
            db.session.add(comm)
            db.session.flush()
            comm_id = comm.comm_id
            try:
                result_line = db.session.query(PosViewModel).filter(
                    order_num=row.order_num, group_name=row.group_name, car=row.car, order_date=row.order_date
                ).all()
                for row_line in result_line:
                    comm_line = CommLineModel(
                        comm_id=comm_id,
                        sale_line_id=row_line.sale_line_id,
                        ticket=row_line.ticket,
                        sale_num=row_line.sale_num,
                        sale_line_num=row_line.sale_line_num,
                        item_no=row_line.item_no,
                        qty=row_line.qty,
                        amt=row_line.amt,
                        created_at=datetime.now(),
                        created_by=user.account,
                        updated_at=datetime.now(),
                        updated_by=user.account
                    )
                    db.session.add(comm_line)
                db.session.flush()
                comm_broker = CommBrokerModel(
                    broker_id=broker_id,
                    comm_id=comm_id,
                    created_at=datetime.now(),
                    created_by=user.account,
                    updated_at=datetime.now(),
                    updated_by=user.account
                )
                db.session.add(comm_broker)
                db.session.flush()
                db.session.commit()
            except Exception as e:
                if comm_id is not None:
                    db.session.rollback()
                return str(e)
        print("寫入comm、comm_line、comm_broker，成功!")
        return "寫入comm、comm_line、comm_broker，成功!"

