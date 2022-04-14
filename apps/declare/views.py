from datetime import datetime
from flask import Blueprint, render_template, request, session, g
import config
from exts import db
from apps.decorators import login_required
from .forms import (
    AddRegisterForm,
    UpdateRegisterForm,
    AddEarnerForm,
    UpdateEarnerForm,
    SwitchEarnerForm,
    AddIncomeForm,
    UpdateIncomeForm,
)
from apps.mc.models import UserModel
from .models import RegisterModel, IdSetModel, IncomeModel
from flask_paginate import Pagination, get_page_parameter
from utils import restful

bp = Blueprint("declare", __name__, url_prefix='/declare')


@bp.route('/registers/',  methods=['GET', 'POST'])
@login_required
def registers():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = RegisterModel.query.order_by(RegisterModel.register_id.desc())
    if request.method == 'POST':
        search = request.values['search']
        if search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(RegisterModel.site_name.like(search_text))
    else:
        search = '請輸入單位名稱'
    register = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'registers': register,
        'pagination': pagination,
        'search': search
    }
    return render_template('declare/registers.html', **context)


@bp.route('/aregister/', methods=['POST'])
@login_required
def aregister():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddRegisterForm(request.form)
    if form.validate():
        uniform_num = form.uniform_num.data
        site_name = form.site_name.data
        register = RegisterModel(uniform_num=uniform_num, site_name=site_name, created_at=created_at,
                                 created_by=created_by, updated_at=updated_at, updated_by=updated_by)
        db.session.add(register)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uregister/', methods=['POST'])
@login_required
def uregister():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateRegisterForm(request.form)
    if form.validate():
        register_id = form.register_id.data
        uniform_num = form.uniform_num.data
        site_name = form.site_name.data
        register = RegisterModel.query.get(register_id)
        if register:
            register.uniform_num = uniform_num
            register.site_name = site_name
            register.updated_at = datetime.now()
            register.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/earners/',  methods=['GET', 'POST'])
@login_required
def earners():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = IdSetModel.query.order_by(IdSetModel.id_no)
    if request.method == 'POST':
        search = request.values['search']
        if search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(IdSetModel.id_name.like(search_text))
    else:
        search = '請輸入所得人姓名'
    earner = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'earners': earner,
        'pagination': pagination,
        'search': search
    }
    return render_template('declare/earners.html', **context)


@bp.route('/aearner/', methods=['POST'])
@login_required
def aearner():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddEarnerForm(request.form)
    if form.validate():
        id_no = form.id_no.data
        id_num = form.id_num.data
        id_name = form.id_name.data
        phone_num = form.phone_num.data
        id_type = form.id_type.data
        id_value_code = form.id_value_code.data
        id_value_name = form.id_value_name.data
        address = form.address.data
        tel = form.tel.data
        id_mark = form.id_mark.data
        remark = form.remark.data
        status = form.status.data
        earner = IdSetModel(
            id_no=id_no, id_num=id_num, id_name=id_name, phone_num=phone_num, id_type=id_type, id_value_code
            =id_value_code, id_value_name=id_value_name, address=address, tel=tel, id_mark=id_mark, remark
            =remark, status=status, created_at=created_at, created_by=created_by, updated_at
            =updated_at, updated_by=updated_by)
        db.session.add(earner)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uearner/', methods=['POST'])
@login_required
def uearner():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateEarnerForm(request.form)
    if form.validate():
        id_id = form.id_id.data
        id_no = form.id_no.data
        id_num = form.id_num.data
        id_name = form.id_name.data
        phone_num = form.phone_num.data
        id_type = form.id_type.data
        id_value_code = form.id_value_code.data
        id_value_name = form.id_value_name.data
        address = form.address.data
        tel = form.tel.data
        id_mark = form.id_mark.data
        remark = form.remark.data
        status = form.status.data
        earner = IdSetModel.query.get(id_id)
        if earner:
            earner.id_id = id_id
            earner.id_no = id_no
            earner.id_num = id_num
            earner.id_name = id_name
            earner.phone_num = phone_num
            earner.id_type = id_type
            earner.id_value_code = id_value_code
            earner.id_value_name = id_value_name
            earner.address = address
            earner.tel = tel
            earner.id_mark = id_mark
            earner.remark = remark
            earner.status = status
            earner.updated_at = datetime.now()
            earner.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/searner/', methods=['POST'])
@login_required
def searner():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = SwitchEarnerForm(request.form)
    if form.validate():
        id_id = form.id_id.data
        earner = IdSetModel.query.get(id_id)
        if earner:
            earner.updated_at = datetime.now()
            earner.updated_by = user.account
            if earner.status == "Y":
                earner.status = "N"
            else:
                earner.status = "Y"
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/incomes/',  methods=['GET', 'POST'])
@login_required
def incomes():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = IncomeModel.query.order_by(IncomeModel.form_id)
    if request.method == 'POST':
        search = request.values['search']
        if search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(IncomeModel.id_name.like(search_text))
    else:
        search = '請輸入所得人姓名'
    income = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'incomes': income,
        'pagination': pagination,
        'search': search
    }
    return render_template('declare/incomes.html', **context)


@bp.route('/aincome/', methods=['POST'])
@login_required
def aincome():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    created_at = datetime.now()
    created_by = user.account
    updated_at = datetime.now()
    updated_by = user.account
    form = AddIncomeForm(request.form)
    if form.validate():
        form_no = form.form_no.data
        uniform_num = form.uniform_num.data
        id_no = form.id_no.data
        earner = IdSetModel.query.filter_by(id_no=id_no).first()
        id_num = earner.id_num
        id_name = earner.id_name
        yyy = form.yyy.data
        mm = form.mm.data
        format = form.format.data
        mark = form.mark.data
        amt = form.amt.data
        tax_amt = form.tax_amt.data
        net_amt = form.net_amt.data
        exe_industry = form.exe_industry.data
        other_income = form.other_income.data
        roya_exp = form.roya_exp.data
        house_tax = form.house_tax.data
        house_add = form.house_add.data
        decl_status = form.decl_status.data
        pay_id = form.pay_id.data
        remark = form.remark.data
        income = IncomeModel(
            form_no=form_no, uniform_num=uniform_num, id_no=id_no, id_num=id_num, id_name=id_name, yyy
            =yyy, mm=mm, format=format, mark=mark, amt=amt, tax_amt=tax_amt, net_amt=net_amt, exe_industry
            =exe_industry, other_income=other_income, roya_exp=roya_exp, house_tax=house_tax, house_add
            =house_add, decl_status=decl_status, pay_id=pay_id, remark=remark, created_at=created_at, created_by
            =created_by, updated_at=updated_at, updated_by=updated_by)
        db.session.add(income)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uincome/', methods=['POST'])
@login_required
def uincome():
    user_id = session.get(config.MC_USER_ID)
    user = UserModel.query.filter_by(user_id=user_id).first()
    form = UpdateIncomeForm(request.form)
    if form.validate():
        form_id = form.form_id.data
        form_no = form.form_no.data
        uniform_num = form.uniform_num.data
        id_no = form.id_no.data
        earner = IdSetModel.query.filter_by(id_no=id_no).first()
        id_num = earner.id_num
        id_name = earner.id_name
        yyy = form.yyy.data
        mm = form.mm.data
        format = form.format.data
        mark = form.mark.data
        amt = form.amt.data
        tax_amt = form.tax_amt.data
        net_amt = form.net_amt.data
        exe_industry = form.exe_industry.data
        other_income = form.other_income.data
        roya_exp = form.roya_exp.data
        house_tax = form.house_tax.data
        house_add = form.house_add.data
        decl_status = form.decl_status.data
        pay_id = form.pay_id.data
        remark = form.remark.data
        income = IncomeModel.query.get(form_no)
        if income:
            income.form_id = form_id
            income.form_no = form_no
            income.uniform_num = uniform_num
            income.id_no = id_no
            income.id_num = id_num
            income.id_name = id_name
            income.yyy = yyy
            income.mm = mm
            income.format = format
            income.mark = mark
            income.amt = amt
            income.tax_amt = tax_amt
            income.net_amt = net_amt
            income.exe_industry = exe_industry
            income.other_income = other_income
            income.roya_exp = roya_exp
            income.house_tax = house_tax
            income.house_add = house_add
            income.decl_status = decl_status
            income.pay_id = pay_id
            income.remark = remark
            income.updated_at = datetime.now()
            income.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dincome/', methods=['POST'])
@login_required
def dincome():
    form_id = request.form.get('form_id')
    if not form_id:
        return restful.params_error(message='請傳入製單流水號！')

    income = IncomeModel.query.get(form_id)
    if not income:
        return restful.params_error(message='沒有這筆資料！')

    db.session.delete(income)
    db.session.commit()
    return restful.success()
