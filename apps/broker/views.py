import config
from datetime import datetime
import apps.config
from flask import Blueprint, render_template, request, session, url_for, redirect
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


@bp.route('/', methods=['GET', 'POST'])
@login_required
def brokers():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = BrokerModel.query.order_by(BrokerModel.broker_id.desc())

    brokers = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'brokers': brokers,
        'pagination': pagination,
    }
    return render_template('broker/brokers.html', **context)


@bp.route('/show_brokers/', methods=['GET', 'POST'])
@login_required
def show_brokers():
    # query_obj = BrokerModel.query.order_by(BrokerModel.broker_id.desc())
    if request.method == 'POST':
        search = request.values['search']
        if search:
            broker = {
                'broker_id': 1,
                'brober_name': '導遊B',
                'phone': '091234567',
            }
            brokers = [broker]
            # search_text = "%{}%".format(search)
            # query_obj = query_obj.filter
    context = {
        'brokers': brokers
    }
    return restful.success(**context)

# @bp.route('/show_brokers/', methods=['GET', 'POST'])
# @login_required
# def show_brokers():
#     query_obj = BrokerModel.query.order_by(BrokerModel.broker_id.desc())
#     if request.method == 'POST':
#         search = request.values['search']
#         if search:
#             search_text = "%{}%".format(search)
#             query_obj = query_obj.filter(BrokerModel.broker_name.like(search_text))
#
#     context = {
#         'brokers': brokers
#     }
#     return render_template('broker/brokers.html')


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
    # 接收list處理完後存入comm, comm_line, comm_broker三張表中
    comm = request.form.getlist('order_num')
    print(comm)

    # 傳遞broker_id去佣金維護畫面
    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'broker': broker
    }
    return redirect(url_for('broker.show_count', **context))


@bp.route('/show_count/', methods=['GET', 'POST'])
@login_required
def show_count():
    # 如何接收redirect所傳過來的broker_id？
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


@bp.route('/ashow_count/', methods=['POST'])
@login_required
def ashow_count():
    return restful.success()


@bp.route('/ushow_count/', methods=['POST'])
@login_required
def ushow_count():
    return restful.success()


@bp.route('/dshow_count/', methods=['POST'])
@login_required
def dshow_count():
    return restful.success()


@bp.route('/check_payment/', methods=['POST'])
@login_required
def check_payment():
    # 接收list存入pay, pay_line兩張表中
    order_num = request.form.getlist('order_num')
    print(order_num)
    # 傳遞broker_id至款管理畫面
    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'broker': broker
    }
    return redirect(url_for('broker.payment', **context))


@bp.route('/payment/', methods=['GET', 'POST'])
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

    broker = {
        'broker_id': '1',
        'broker_name': '導遊Ａ'
    }

    context = {
        'payments': payments,
        'broker': broker
    }
    return render_template("/broker/payments.html", **context)


@bp.route('/apayment/', methods=['POST'])
@login_required
def apayment():
    return restful.success()


@bp.route('/upayment/', methods=['POST'])
@login_required
def upayment():
    return restful.success()


@bp.route('/dpayment/', methods=['POST'])
@login_required
def dpayment():
    return restful.success()

