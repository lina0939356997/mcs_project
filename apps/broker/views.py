import config
from datetime import datetime
import apps.config
from flask import Blueprint, render_template, request, session
from .forms import (
    TakeComm,
)
from apps.mc.models import UserModel
from ..models import PosViewModel
from flask_paginate import Pagination, get_page_parameter
from .models import CommModel, CommLineModel, BrokerModel, CommBrokerModel
from apps.decorators import login_required
from sqlalchemy import func
from exts import db
from utils import restful

bp = Blueprint("broker", __name__, url_prefix='/broker')

@bp.route('/show_count/')
@login_required
def show_count():
    return render_template('broker/brokermaintenances.html')

@bp.route('/')
@login_required
def show_comms():
    # pending = db.session.query(PosViewModel).filter(PosViewModel.sale_line_id.notin_(CommLineModel.sale_line_id))
    # pending = db.session.query(PosViewModel).filter(PosViewModel.sale_line_id.isnot(None))
    # result = db.session.query(PosViewModel).select_from(
    #     PosViewModel, PosViewModel.sale_line_id == CommLineModel.sale_line_id).order_by(PosViewModel.sale_line_id).all()
    # print(result)
    result = db.session.query(
        PosViewModel.order_num,
        PosViewModel.group_name,
        PosViewModel.car,
        PosViewModel.order_date,
        func.sum(PosViewModel.amt).label('subtotal')
    ).filter(PosViewModel.sale_line_id.isnot(None)) \
        .group_by(PosViewModel.order_num,
                  PosViewModel.group_name,
                  PosViewModel.car,
                  PosViewModel.order_date) \
        .all()

    brokers = BrokerModel.query.order_by(BrokerModel.broker_id)

    context = {
        'commissions': result,
        'brokers': brokers
    }

    return render_template('broker/brokers.html', **context)


@bp.route('/distribute/', methods=['GET', 'POST'])
@login_required
def distribute():
    # pending = db.session.query(PosViewModel).filter(PosViewModel.sale_line_id.notin_(CommLineModel.sale_line_id))
    order_num_list = request.args.getlist('order_num')
    group_name_list = request.args.getlist('group_name')
    car_list = request.args.getlist('car')
    order_date_list = request.args.getlist('')
    form = TakeComm(request.form)
    if form.validate():
        order_num = form.order_num.data
        group_name = form.group_name.data
        car = form.car.data
        order_date = form.order_date.data
        broker_id = form.broker_id.date

        result = db.session.query(
            PosViewModel.order_num,
            PosViewModel.group_name,
            PosViewModel.car,
            PosViewModel.order_date,
            func.sum(PosViewModel.amt).label('subtotal')
        ).filter(
            order_num == PosViewModel.order_num,
            group_name == PosViewModel.group_name,
            car == PosViewModel.car,
            order_date == PosViewModel.order_date
        ).group_by(
            PosViewModel.order_num,
            PosViewModel.group_name,
            PosViewModel.car,
            PosViewModel.order_date).all()
        user_id = session.get(config.MC_USER_ID)
        user = UserModel.query.filter_by(user_id=user_id).first()
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

