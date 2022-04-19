import config
from datetime import datetime
import apps.config
from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import (
    AddBrokerForm,
    UpdateBrokerForm,
    TakeComm,
)
from apps.mc.models import UserModel
from ..models import PosViewModel
from flask_paginate import Pagination, get_page_parameter
from .models import CommModel, CommLineModel, BrokerModel
from apps.decorators import login_required
from sqlalchemy import func
from exts import db
from utils import restful
from .library import calculate_comm, select_broker_comm

bp = Blueprint("broker", __name__, url_prefix='/broker')

@bp.route('/salesheet/', methods=['GET', 'POST'])
@login_required
def salesheet():
    order_num = request.args.get('order_num')
    print(order_num)
    return render_template('broker/salesheet.html')

@bp.route('/brokerinfors/', methods=['GET', 'POST'])
@login_required
def brokerinfors():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = BrokerModel.query.order_by(BrokerModel.broker_id.desc())
    if request.method == 'POST':
        search = request.values['search']
        a = ord(search[0])
        if search and a < 58:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(BrokerModel.phone.like(search_text))
        elif search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(BrokerModel.broker_name.like(search_text))
    else:
        search = '請輸入導遊名稱或電話'
    broker = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'brokers': broker,
        'pagination': pagination,
        'search': search
    }
    return render_template('broker/brokerinfors.html', **context)


@bp.route('/abrokerinfor/', methods=['POST'])
@login_required
def abrokerinfor():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddBrokerForm(request.form)
    if form.validate():
        broker_name = form.broker_name.data
        broker_num = form.broker_num.data
        travel = form.travel.data
        phone = form.phone.data
        address = form.address.data
        broker = BrokerModel(broker_name=broker_name, broker_num=broker_num, travel=travel, phone=phone, address
                             =address, created_at=created_at, created_by=created_by, updated_at=updated_at, updated_by
                             =updated_by)
        db.session.add(broker)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/ubrokerinfor/', methods=['POST'])
@login_required
def ubrokerinfor():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateBrokerForm(request.form)
    if form.validate():
        broker_id = form.broker_id.data
        broker_name = form.broker_name.data
        broker_num = form.broker_num.data
        travel = form.travel.data
        phone = form.phone.data
        address = form.address.data
        register = BrokerModel.query.get(broker_id)
        if register:
            register.broker_name = broker_name
            register.broker_num = broker_num
            register.travel = travel
            register.phone = phone
            register.address = address
            register.updated_at = datetime.now()
            register.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dbrokerinfor/', methods=['POST'])
@login_required
def dbrokerinfor():
    broker_id = request.form.get('broker_id')
    if not broker_id:
        return restful.params_error(message='id缺失！')

    broker = BrokerModel.query.get(broker_id)
    if not broker:
        return restful.params_error(message='沒有這筆資料！')

    db.session.delete(broker)
    db.session.commit()
    return restful.success()


@bp.route('/show_comms/', methods=['GET', 'POST'])
@login_required
def show_comms():
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

    # 不可以直接按搜尋
    if request.method == 'POST':
        search = request.values['search']
        a = ord(search[0])
        if a < 58:
            search_text = "%{}%".format(search)
            query_obj = BrokerModel.query.filter(BrokerModel.phone.like(search_text))
        else:
            search_text = "%{}%".format(search)
            query_obj = BrokerModel.query.filter(BrokerModel.broker_name.like(search_text))

        brokers = query_obj.slice(0, 10)

        context = {
            'commissions': result,
            'brokers': brokers
        }
        return render_template('broker/brokers.html', **context)
    else:
        context = {
            'commissions': result,
        }
        return render_template('broker/brokers.html', **context)


@bp.route('/show_count/', methods=['GET', 'POST'])
@login_required
def show_count():
    comm_key = request.form.getlist('comm_key')
    print(comm_key)
    broker_id = request.form.get('brokerchose')
    print(broker_id)
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

    # broker = {
    #     'broker_id': broker_id,
    #     'broker_name': '導遊B',
    #     'phone': '091234567'
    # }
# --------------------------------------------------------------------------------------------
    if request.method == 'POST':
        # 有傳入需要計算的資料及broker_id，去pos系統抓取資料存入資料庫後再顯示該broker所擁有未結算的comm
        if comm_key and broker_id:
            calculate_comm(comm_key, broker_id)
            result = select_broker_comm(broker_id)
            print(result)
            broker = BrokerModel.query.filter(BrokerModel.broker_id == broker_id).first()
            context = {
                'comms': comms,
                'broker': broker
            }
            return render_template('broker/brokermaintenances.html', **context)
        # 只有傳入broker_id，去comm表抓取屬於該broker的所有未結算的資料
        elif broker_id:
            print("沒有要分配的佣金")
            result = select_broker_comm(broker_id)
            print(result)
            broker = BrokerModel.query.filter(BrokerModel.broker_id == broker_id).first()
            context = {
                'comms': comms,
                'broker': broker
            }
            return render_template('broker/brokermaintenances.html', **context)
        # 什麼都沒有傳入，需要先傳入broker_id才能進行後續的操作
        else:
            print("啥都沒有")
            search = request.values['search']
            a = ord(search[0])
            if a < 58:
                search_text = "%{}%".format(search)
                query_obj = BrokerModel.query.filter(BrokerModel.phone.like(search_text))
            else:
                search_text = "%{}%".format(search)
                query_obj = BrokerModel.query.filter(BrokerModel.broker_name.like(search_text))

            brokers = query_obj.all()
            context = {
                'comms': comms,
                'broker': brokers
            }
            return render_template('broker/brokermaintenances.html', **context)
    # 直接進進入
    else:
        context = {
            'comms': comms,
            'broker': None
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
    broker_id = request.form.get('brokerchose')
    print(broker_id)
    # 接收list存入pay, pay_line兩張表中
    order_num = request.form.getlist('order_num')
    print(order_num)
    # 傳遞broker_id至款管理畫面
    broker = {
        'broker_id': broker_id,
        'broker_name': '導遊B',
        'phone': '091234567'
    }

    context = {
        'broker': broker
    }
    return redirect(url_for('broker.payment', **context))


@bp.route('/payment/', methods=['GET', 'POST'])
@login_required
def payment():
    broker_id = request.form.get('brokerchose')
    print(broker_id)
    payment1 = {
        'pay_date': '2020, 04, 12',
        'pay_status': '已付款',
        'total_amt': 2000,
    }

    payment2 = {
        'pay_date': '2020, 04, 11',
        'pay_status': '未付款',
        'total_amt': 6000
    }
    payments = [payment1, payment2]

    broker = {
        'broker_id': broker_id,
        'broker_name': '導遊B',
        'phone': '091234567'
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

