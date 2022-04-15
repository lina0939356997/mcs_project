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


@bp.route('/show_comms/', methods=['GET', 'POST'])
@login_required
def show_comms():
    # result = db.session.query(
    #     PosViewModel.order_num,
    #     PosViewModel.group_name,
    #     PosViewModel.car,
    #     PosViewModel.order_date,
    #     func.sum(PosViewModel.amt).label('subtotal')
    # ).filter(PosViewModel.sale_line_id.isnot(None)) \
    #     .group_by(PosViewModel.order_num,
    #               PosViewModel.group_name,
    #               PosViewModel.car,
    #               PosViewModel.order_date) \
    #     .all()

    # broker = BrokerModel.query.order_by(BrokerModel.broker_id)

    commission1 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'A車',
        'order_date': '2022, 4, 15',
        'subtotal': 20000
    }

    commission2 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'B車',
        'order_date': '2022, 4, 15',
        'subtotal': 15000
    }

    commissions = [commission1, commission2]

    context = {
        'commissions': commissions,
        'broker': broker
    }
    return render_template('broker/brokers.html', **context)


@bp.route('/distribute/', methods=['POST'])
@login_required
def distribute():
    # 接收list存入comm, comm_line, comm_broker三張表中
    # group_name = request.args.getList('group_name')
    # car = request.args.getList('car')
    # subtotal = request.args.getList('subtotal')
    # print(group_name)
    # print(car)
    # print(subtotal)
    # 從comm_broker關聯到comm表中取出屬於該broker的comm資料
    comm1 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'A車',
        'order_date': '2022, 4, 15',
        'sale_amt': 20000,
        'comm_amt': 2000
    }

    comm2 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'B車',
        'order_date': '2022, 4, 15',
        'sale_amt': 15000,
        'comm_amt': 1500
    }
    comms = [comm1, comm2]

    broker = [{
        broker_id: '1',
        broker_name: '導遊Ａ'
    }]

    context = {
        'comms': comms,
        'broker': broker
    }
    return render_template("broker/brokermaintains.html", **context)


@bp.route('/payment/', methods=['PSST'])
@login_required
def payment():
    return restful_template("/broker/payment.html")




