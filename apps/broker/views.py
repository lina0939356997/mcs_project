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


@bp.route('/show_count/', methods=['GET', 'POST'])
@login_required
def show_count():
    if request.method == 'POST':
        broker_id = 1
    else:
        broker_id = None

    commissions = {
        'order_num': "1",
        'group_name': "佐登妮斯旅行團",
        'car': "A車",
        'order_date': "2020/04/15",
        'broker_id': broker_id
    }
    context = {
        'commissions': commissions
    }
    return render_template('broker/brokercount.html', **context)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def show_comms():

    return render_template("broker/brokers.html")


@bp.route('/distribute/', methods=['GET', 'POST'])
@login_required
def distribute():
    return render_template("broker/brokermaintains.html")

