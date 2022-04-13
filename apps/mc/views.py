import datetime

from flask import Blueprint, render_template, views, request, redirect, session, url_for, g

import config
from exts import db, mail
from .decorators import login_required
from .forms import (
    LoginForm,
    AddUsersetForm,
    UpdateUsersetForm,
    AddReportinformForm,
    AddListvalueForm,
    UpdateListvalueForm,
    UpdateReportinformForm,
    AddEarnerinformForm,
    UpdateEarnerForm,
    SwitchEarnerForm,
    IncomeDataForm,
)
from .models import MCUser
from ..models import *
from flask_paginate import Pagination, get_page_parameter
from utils import restful

bp = Blueprint("mc", __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    return render_template('mc/mc_index.html')


@bp.route('/usersets/')
@login_required
def usersets():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = MCUser.query.order_by(MCUser.user_id.desc())

    usersets = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'usersets': usersets,
        'pagination': pagination,
    }
    return render_template('mc/mc_usersets.html', **context)


@bp.route('/auserset/', methods=['POST'])
@login_required
def auserset():
    form = AddUsersetForm(request.form)
    if form.validate():
        account = form.account.data
        password = form.password.data
        name = form.name.data
        permission = form.permission.data
        user = MCUser(account=account, password=password, name=name, permission=permission)
        db.session.add(user)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uuserset/', methods=['POST'])
@login_required
def uuserset():
    form = UpdateUsersetForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        account = form.account.data
        password = form.password.data
        name = form.name.data
        permission = form.permission.data
        userset = MCUser.query.get(user_id)
        if userset:
            userset.account = account
            userset.password = password
            userset.name = name
            userset.permission = permission
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

    userset = MCUser.query.get(user_id)
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
    return render_template('mc/mc_sysparameters.html', **context)


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
    return render_template('mc/mc_listvalues.html', **context)


@bp.route('/alistvalue/', methods=['POST'])
@login_required
def alistvalue():
    form = AddListvalueForm(request.form)
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    creation_date = datetime.now()
    # creation_by = db.session.query(MCUser.account).all()
    creation_by = user.account
    updated_date = datetime.now()
    # updated_by = db.session.query(MCUser.account).all()
    updated_by = user.account
    if form.validate():
        set_type = form.set_type.data
        value_code = form.value_code.data
        value_name = form.value_name.data
        value_desc = form.value_desc.data
        parent_value = form.parent_value.data
        listvalue = ListvalueModel(
            set_type=set_type, value_code=value_code, value_name=value_name, value_desc=value_desc, parent_value
            =parent_value, creation_date=creation_date, creation_by=creation_by, updated_date=updated_date, updated_by
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
    user = MCUser.query.filter_by(user_id=user_id).first()
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
            listvalue.updated_date = datetime.now()
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


@bp.route('/reportinforms/',  methods=['GET', 'POST'])
@login_required
def reportinforms():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = ReportBasicInformModel.query.order_by(ReportBasicInformModel.register_id.desc())
    if request.method == 'POST':
        search = request.values['search']
        if search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(ReportBasicInformModel.site_name.like(search_text))
    else:
        search = '請輸入單位名稱'
    reportinforms = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'reportinforms': reportinforms,
        'pagination': pagination,
        'search': search
    }
    return render_template('mc/mc_reportinforms.html', **context)


@bp.route('/areportinform/', methods=['POST'])
@login_required
def areportinform():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    creation_date = datetime.now()
    creation_by = user.account
    updated_date = datetime.now()
    updated_by = user.account
    form = AddReportinformForm(request.form)
    if form.validate():
        uniform_num = form.uniform_num.data
        site_name = form.site_name.data
        reportinform = ReportBasicInformModel(uniform_num=uniform_num, site_name=site_name, creation_date=creation_date,
                                              creation_by=creation_by, updated_date=updated_date, updated_by
                                              =updated_by)
        db.session.add(reportinform)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/ureportinform/', methods=['POST'])
@login_required
def ureportinform():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    form = UpdateReportinformForm(request.form)
    if form.validate():
        register_id = form.register_id.data
        uniform_num = form.uniform_num.data
        site_name = form.site_name.data
        reportinform = ReportBasicInformModel.query.get(register_id)
        if reportinform:
            reportinform.uniform_num = uniform_num
            reportinform.site_name = site_name
            reportinform.updated_date = datetime.now()
            reportinform.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/earnerinforms/',  methods=['GET', 'POST'])
@login_required
def earnerinforms():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = 0
    query_obj = None
    query_obj = EarnerBasicInformModel.query.order_by(EarnerBasicInformModel.id_no)
    if request.method == 'POST':
        search = request.values['search']
        if search:
            search_text = "%{}%".format(search)
            query_obj = query_obj.filter(EarnerBasicInformModel.id_name.like(search_text))
    else:
        search = '請輸入所得人姓名'
    earnerinforms = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'earnerinforms': earnerinforms,
        'pagination': pagination,
        'search': search
    }
    return render_template('mc/mc_earnerinforms.html', **context)


@bp.route('/aearnerinform/', methods=['POST'])
@login_required
def aearnerinform():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    creation_date = datetime.now()
    creation_by = user.account
    updated_date = datetime.now()
    updated_by = user.account
    form = AddEarnerinformForm(request.form)
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
        earnerinform = EarnerBasicInformModel(
            id_no=id_no, id_num=id_num, id_name=id_name, phone_num=phone_num, id_type=id_type, id_value_code
            =id_value_code, id_value_name=id_value_name, address=address, tel=tel, id_mark=id_mark, remark
            =remark, status=status, creation_date=creation_date, creation_by=creation_by, updated_date
            =updated_date, updated_by=updated_by)
        db.session.add(earnerinform)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uearnerinform/', methods=['POST'])
@login_required
def uearnerinform():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    form = UpdateEarnerForm(request.form)
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
        earnerinform = EarnerBasicInformModel.query.get(id_no)
        if earnerinform:
            earnerinform.id_no = id_no
            earnerinform.id_num = id_num
            earnerinform.id_name = id_name
            earnerinform.phone_num = phone_num
            earnerinform.id_type = id_type
            earnerinform.id_value_code = id_value_code
            earnerinform.id_value_name = id_value_name
            earnerinform.address = address
            earnerinform.tel = tel
            earnerinform.id_mark = id_mark
            earnerinform.remark = remark
            earnerinform.status = status
            earnerinform.updated_date = datetime.now()
            earnerinform.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/searnerinform/', methods=['POST'])
@login_required
def searnerinform():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    form = SwitchEarnerForm(request.form)
    if form.validate():
        id_no = form.id_no.data
        status = form.status.data
        earnerinform = EarnerBasicInformModel.query.get(id_no)
        if earnerinform:
            earnerinform.updated_date = datetime.now()
            earnerinform.updated_by = user.account
            earnerinform.status = status
            if earnerinform.status:
                earnerinform.status = False
            else:
                earnerinform.status = True
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/incomedatas/',  methods=['GET', 'POST'])
@login_required
def incomedatas():
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
    incomedatas = query_obj.slice(start, end)
    total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    context = {
        'incomedatas': incomedatas,
        'pagination': pagination,
        'search': search
    }
    return render_template('mc/mc_incomedatas.html', **context)


@bp.route('/aincomedata/', methods=['POST'])
@login_required
def aincomedata():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    creation_date = datetime.now()
    creation_by = user.account
    updated_date = datetime.now()
    updated_by = user.account
    form = IncomeDataForm(request.form)
    if form.validate():
        form_id = form.form_id.data
        uniform_num = form.uniform_num.data
        id_no = form.id_no.data
        earner = EarnerBasicInformModel.query.filter_by(id_no=id_no).first()
        id_num = earner.id_num
        id_name = earner.id_name
        income_yyy = form.income_yyy.data
        income_mm = form.income_mm.data
        income_format = form.income_format.data
        income_mark = form.income_mark.data
        income_amt = form.income_amt.data
        tax_amt = form.tax_amt.data
        net_amt = form.net_amt.data
        exe_industry = form.exe_industry.data
        other_income = form.other_income.data
        royalties_exp = form.royalties_exp.data
        house_tax_num = form.house_tax_num.data
        house_address = form.house_address.data
        declare_status = form.declare_status.data
        comm_flag = False
        comm_id = 1
        remark = form.remark.data
        incomedata = IncomeModel(
            form_id=form_id, uniform_num=uniform_num, id_no=id_no, id_num=id_num, id_name=id_name, income_yyy
            =income_yyy, income_mm=income_mm, income_format=income_format, income_mark=income_mark, income_amt
            =income_amt, tax_amt=tax_amt, net_amt=net_amt, exe_industry=exe_industry, other_income
            =other_income, royalties_exp=royalties_exp, house_tax_num=house_tax_num, house_address
            =house_address, declare_status=declare_status, comm_flag=comm_flag, comm_id=comm_id, remark
            =remark, creation_date=creation_date, creation_by=creation_by, updated_date=updated_date, updated_by
            =updated_by)
        db.session.add(incomedata)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uincomedata/', methods=['POST'])
@login_required
def uincomedata():
    user_id = session.get(config.MC_USER_ID)
    user = MCUser.query.filter_by(user_id=user_id).first()
    form = IncomeDataForm(request.form)
    if form.validate():
        form_id = form.form_id.data
        uniform_num = form.uniform_num.data
        id_no = form.id_no.data
        earner = EarnerBasicInformModel.query.filter_by(id_no=id_no).first()
        id_num = earner.id_num
        id_name = earner.id_name
        income_yyy = form.income_yyy.data
        income_mm = form.income_mm.data
        income_format = form.income_format.data
        income_mark = form.income_mark.data
        income_amt = form.income_amt.data
        tax_amt = form.tax_amt.data
        net_amt = form.net_amt.data
        exe_industry = form.exe_industry.data
        other_income = form.other_income.data
        royalties_exp = form.royalties_exp.data
        house_tax_num = form.house_tax_num.data
        house_address = form.house_address.data
        declare_status = form.declare_status.data
        comm_flag = True
        comm_id = 2
        remark = form.remark.data
        incomedata = IncomeModel.query.get(form_id)
        if incomedata:
            incomedata.form_id = form_id
            incomedata.uniform_num = uniform_num
            incomedata.id_no = id_no
            incomedata.id_num = id_num
            incomedata.id_name = id_name
            incomedata.income_yyy = income_yyy
            incomedata.income_mm = income_mm
            incomedata.income_format = income_format
            incomedata.income_mark = income_mark
            incomedata.income_amt = income_amt
            incomedata.tax_amt = tax_amt
            incomedata.net_amt = net_amt
            incomedata.exe_industry = exe_industry
            incomedata.other_income = other_income
            incomedata.royalties_exp = royalties_exp
            incomedata.house_tax_num = house_tax_num
            incomedata.house_address = house_address
            incomedata.declare_status = declare_status
            incomedata.comm_flag = comm_flag
            incomedata.comm_id = comm_id
            incomedata.remark = remark
            incomedata.updated_date = datetime.now()
            incomedata.updated_by = user.account
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='沒有這筆資料！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dincomedata/', methods=['POST'])
@login_required
def dincomedata():
    form_id = request.form.get('form_id')
    if not form_id:
        return restful.params_error(message='請傳入製單流水號！')

    incomedata = IncomeModel.query.get(form_id)
    if not incomedata:
        return restful.params_error(message='沒有這筆資料！')

    db.session.delete(incomedata)
    db.session.commit()
    return restful.success()


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('mc/mc_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            account = form.account.data
            password = form.password.data
            session['account'] = account
            user = MCUser.query.filter_by(account=account).first()
            if user and user.password == password:
                session[config.MC_USER_ID] = user.user_id
                return redirect(url_for('mc.index'))
            else:
                return self.get(message='登入失敗，請從新輸入用戶資訊!')
        else:
            message = form.get_error()
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
