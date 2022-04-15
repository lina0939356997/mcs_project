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
    if request.method == 'POST':
        broker_id = 1
    else:
        broker_id = None

    commissions = {
        'order_num': "1",
        'group_name': "佐登妮斯旅行團",
        'car': "A車",
        'order_date': "2020/04/15",
        'subtotal': 20000
    }
    broker = {
        'broker_id': broker_id
    }
    context = {
        'commissions': commissions,
        'broker': broker
    }
    return render_template('broker/brokercount.html', **context)


@bp.route('/distribute/', methods=['GET', 'POST'])
@login_required
def distribute():
    group_name = request.args.getList('group_name')
    car = request.args.getList('car')
    subtotal = request.args.getList('subtotal')
    print(group_name)
    print(car)
    print(subtotal)
    return render_template("broker/brokermaintains.html")

