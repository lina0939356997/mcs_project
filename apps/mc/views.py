import datetime
from flask import Blueprint, render_template, views, request, redirect, session, url_for
import config
from exts import db
from apps.decorators import login_required
from .forms import (
    LoginForm,
    AddUsersetForm,
    UpdateUsersetForm,
    AddListvalueForm,
    UpdateListvalueForm,
)
from .models import UserModel, ListvalueModel
from flask_paginate import Pagination, get_page_parameter
from utils import restful

bp = Blueprint("mc", __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    return render_template('mc/index.html')


@bp.route('/usersets/')
@login_required
def usersets():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = UserModel.query.order_by(UserModel.user_id.desc())

    usersets = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'usersets': usersets,
        'pagination': pagination,
    }
    return render_template('mc/usersets.html', **context)


@bp.route('/auserset/', methods=['POST'])
@login_required
def auserset():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddUsersetForm(request.form)
    if form.validate():
        account = form.account.data
        password = form.password.data
        name = form.name.data
        permission = form.permission.data
        user = UserModel(account=account, password=password, name=name, permission=permission, created_at=created_at,
                         created_by=created_by, updated_at=updated_at, updated_by=updated_by)
        db.session.add(user)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uuserset/', methods=['POST'])
@login_required
def uuserset():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateUsersetForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        account = form.account.data
        password = form.password.data
        name = form.name.data
        permission = form.permission.data
        userset = UserModel.query.get(user_id)
        if userset:
            userset.account = account
            userset.password = password
            userset.name = name
            userset.permission = permission
            userset.updated_at = datetime.now()
            userset.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/duserset/', methods=['POST'])
@login_required
def duserset():
    user_id = request.form.get('user_id')
    if not user_id:
        return restful.params_error(message='請傳入ID！')

    userset = UserModel.query.get(user_id)
    if not userset:
        return restful.params_error(message='沒有這筆資料！')

    db.session.delete(userset)
    db.session.commit()
    return restful.success()


@bp.route('/sysparameters/', methods=['GET'])
@login_required
def sysparameters():
    context = {
        "WebName": "MetaCommission",
        "WebTitle": "MetaCommission",
        "BaseAmount": 25250,
        "HealthyRate": 2.11,
        "DefIncomeCode": "50",
        "DefUniformNum": "89826011"
    }
    return render_template('mc/sysparameters.html', **context)


@bp.route('/listvalues/', methods=['GET', 'POST'])
@login_required
def listvalues():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = ListvalueModel.query.order_by(ListvalueModel.set_value_id.desc())

    listvalues = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'listvalues': listvalues,
        'pagination': pagination,
    }
    return render_template('mc/listvalues.html', **context)


@bp.route('/alistvalue/', methods=['POST'])
@login_required
def alistvalue():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddListvalueForm(request.form)
    if form.validate():
        set_type = form.set_type.data
        value_code = form.value_code.data
        value_name = form.value_name.data
        value_desc = form.value_desc.data
        parent_value = form.parent_value.data
        listvalue = ListvalueModel(
            set_type=set_type, value_code=value_code, value_name=value_name, value_desc=value_desc, parent_value
            =parent_value, created_at=created_at, created_by=created_by, updated_at=updated_at, updated_by
            =updated_by)
        db.session.add(listvalue)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/ulistvalue/', methods=['POST'])
@login_required
def ulistvalue():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateListvalueForm(request.form)
    if form.validate():
        set_value_id = form.set_value_id.data
        set_type = form.set_type.data
        value_code = form.value_code.data
        value_name = form.value_name.data
        value_desc = form.value_desc.data
        parent_value = form.parent_value.data
        listvalue = ListvalueModel.query.get(set_value_id)
        if listvalue:
            listvalue.set_type = set_type
            listvalue.value_code = value_code
            listvalue.value_name = value_name
            listvalue.value_desc = value_desc
            listvalue.parent_value = parent_value
            listvalue.updated_at = datetime.now()
            listvalue.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dlistvalue/', methods=['POST'])
@login_required
def dlistvalue():
    set_value_id = request.form.get('set_value_id')
    if not set_value_id:
        return restful.params_error(message='請傳入ID！')

    listvalue = ListvalueModel.query.get(set_value_id)
    if not listvalue:
        return restful.params_error(message='沒有這筆資料！')

    db.session.delete(listvalue)
    db.session.commit()
    return restful.success()


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('mc/login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            account = form.account.data
            password = form.password.data
            session['account'] = account
            user = UserModel.query.filter_by(account=account).first()
            if user and user.password == password:
                session[config.MC_USER_ID] = user.user_id
                return redirect(url_for('mc.index'))
            else:
                return self.get(message='登入失敗，請從新輸入用戶資訊!')
        else:
            message = form.get_error()
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
