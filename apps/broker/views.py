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
    commission1 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'A車',
        'order_date': '2022, 4, 15',
        'subtotal': 20000,
    }

    commission2 = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'B車',
        'order_date': '2022, 4, 15',
        'subtotal': 15000
    }

    commissions = [commission1, commission2]

    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'commissions': commissions,
        'broker': broker
    }
    return render_template('broker/brokers.html', **context)


@bp.route('/distribute/', methods=['POST'])
@login_required
def distribute():
    # 接收list存入comm, comm_line, comm_broker三張表中
    order_num = request.form.getlist('order_num')
    group_name = request.form.getlist('group_name')
    car = request.form.getlist('car')
    order_date = request.form.getlist('order_date')
    print(order_num)
    print(group_name)
    print(car)
    print(order_date)
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

    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'comms': comms,
        'broker': broker
    }
    return render_template("broker/brokermaintenances.html", **context)


@bp.route('/show_count/', methods=['GET', 'POST'])
@login_required
def show_count():
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

    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'comms': comms,
        'broker': broker
    }
    return render_template('broker/brokermaintenances.html', **context)


@bp.route('/payment/', methods=['PSST'])
@login_required
def payment():
    payment1 = {
        'pay_date': '2020, 04, 12',
        'pay_status': '已付款',
        'total_amt': 2000,
    }

    payment2 = {
        'pay_date': '2020, 04, 11',
        'pay_status': '已付款',
        'total_amt': 6000
    }
    payments = [payment1, payment2]
    context = {
        payments,
    }
    return restful_template("/broker/payments.html", **context)




