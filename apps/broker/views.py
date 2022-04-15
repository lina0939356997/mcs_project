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

    commission = {
        'order_num': '1',
        'group_name': '佐登尼斯旅行團',
        'car': 'A車',
        'order_date': '2022, 4, 15',
        'subtotal': 20000
    }

    result = [commission]

    broker = BrokerModel.query.order_by(BrokerModel.broker_id)

    context = {
        'commissions': result,
        'broker': broker
    }
    print(result)
    return render_template('broker/brokers.html', **context)


@bp.route('/distribute/', methods=['POST'])
@login_required
def distribute():
    group_name = request.args.getList('group_name')
    car = request.args.getList('car')
    subtotal = request.args.getList('subtotal')
    print(group_name)
    print(car)
    print(subtotal)
    return render_template("broker/brokermaintains.html")


@bp.route('/payment/', methods=['PSST'])
@login_required
def payment():
    return restful_template("/broker/payment.html")




