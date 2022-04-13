import config
import datetime
from ..models import PosViewModel
from flask import Blueprint, render_template
from flask_paginate import Pagination, get_page_parameter
from .models import CommModel, CommLineModel
from apps.decorators import login_required
from sqlalchemy import func
from exts import db
from utils import restful

bp = Blueprint("broker", __name__, url_prefix='/broker')


@bp.route('/')
@login_required
def show_comm():
    result = db.session.query(
        PosViewModel.order_num,
        PosViewModel.group_name,
        PosViewModel.car,
        PosViewModel.order_date,
        func.sum(PosViewModel.amt).label('subtotal')
    ).filter(PosViewModel.sale_line_id.notin_(CommLineModel.sale_line_id)) \
        .group_by(PosViewModel.order_num,
                  PosViewModel.group_name,
                  PosViewModel.car,
                  PosViewModel.order_date) \
        .all()

    context = {
        'rewords': result,
    }

    return render_template('broker/broker.html', **context)







