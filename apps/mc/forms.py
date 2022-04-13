from wtforms import StringField, IntegerField, FloatField, SelectField, BooleanField
from wtforms.validators import Email, InputRequired, Length, EqualTo, DataRequired
from wtforms import ValidationError
from flask import g
from ..forms import BaseForm


class LoginForm(BaseForm):
    account = StringField(validators=[Length(1, 10, message='帳號不可超過10個字元'), InputRequired(message='請輸入帳號!')])
    password = StringField(validators=[Length(8, 10, message='密碼介於8~10個字元'), InputRequired(message='請輸入密碼!')])


class AddUsersetForm(BaseForm):
    account = StringField(validators=[Length(1, 10, message='帳號不可超過10個字元'), InputRequired(message='請輸入帳號！')])
    password = StringField(validators=[Length(8, 10, message='密碼介於8~10個字元'), InputRequired(message='請輸入密碼！')])
    name = StringField(validators=[Length(1, 20, message='姓名不可超過20個字元'), InputRequired(message='請輸入姓名！')])
    permission = SelectField('權限', choices=[('admin', 'admin'), ('user', 'user')]
                             , validators=[DataRequired(message='請輸入權限等級！')], coerce=str)


class UpdateUsersetForm(AddUsersetForm):
    user_id = IntegerField(validators=[InputRequired(message='id缺失！')])


class AddListvalueForm(BaseForm):
    set_type = StringField(validators=[Length(1, 30, message='清單類別值不可超過30個字元'),
                                       InputRequired(message='請輸入清單值類別!')])
    value_code = StringField(validators=[Length(0, 10, message='清單值代碼不可超過10個字元')])
    value_name = StringField(validators=[Length(1, 100, message='清單值不可超過100個字元'),
                                         InputRequired(message='請輸入清單值!')])
    value_desc = StringField(validators=[Length(0, 200, message='清單值描述不可超過200個字元')])
    parent_value = StringField(validators=[Length(0, 10, message='ParentValue不可超過10個字元')])


class UpdateListvalueForm(AddListvalueForm):
    set_value_id = IntegerField(validators=[InputRequired(message='id缺失!')])


class AddReportinformForm(BaseForm):
    uniform_num = StringField(validators=[Length(8, 8, message='統一編號為8個字元'),
                                          InputRequired(message='請輸入統一編號')])
    site_name = StringField(validators=[Length(1, 30, message='單位名稱不可超過30個字元'),
                                        InputRequired(message='請輸入單位名稱')])


class UpdateReportinformForm(AddReportinformForm):
    register_id = IntegerField(validators=[InputRequired(message='id缺失!')])


class AddEarnerinformForm(BaseForm):
    id_no = StringField(validators=[Length(1, 12, message='所得人代號不可超過12個字元'),
                                    InputRequired(message='請填入所得人代號!')])
    id_num = StringField(validators=[Length(1, 10, message='所得人統一編(證)號不可超過10個字元'),
                                     InputRequired(message='請填入所得人統一編(證)號!')])
    id_name = StringField(validators=[Length(1, 50, message='所得人姓名不可超過50個字元'),
                                      InputRequired(message='請填入所得人姓名!')])
    phone_num = StringField(validators=[Length(1, 10, message='手機號碼不可超過10個字元'),
                                        InputRequired(message='請填入手機號碼!')])
    id_type = SelectField('證號別', choices=[('A', '境內居住者'), ('B', '非境內居住者')], validators=[
        InputRequired(message='請填入證號別!')], coerce=str)
    id_value_code = StringField(validators=[Length(1, 10, message='證號別選單值不可超過10個字元'),
                                            InputRequired(message='請輸入證號別選單值!')])
    id_value_name = StringField(validators=[Length(1, 100, message='證號別選單內容不可超過100個字元'),
                                            InputRequired(message='請輸入證號別選單內容!')])
    address = StringField(Length(0, 200, message='所得人住址不可超過200個字元'),)
    tel = StringField(Length(0, 20, message='所得人電話不可超過20個字元'),)
    id_mark = StringField(validators=[Length(1, 10, message='所得人註記不可超過10個字元'),
                                      InputRequired(message='請填入所得人註記!')])
    remark = StringField(Length(0, 200, message='所得人備註不可超過200個字元'),)
    status = BooleanField(validators=[InputRequired(message='請選擇狀態!')])


class UpdateEarnerForm(AddEarnerinformForm):
    id_no = StringField(validators=[InputRequired(message='所得人代號缺失!')])


class SwitchEarnerForm(BaseForm):
    id_no = StringField(validators=[InputRequired(message='所得人代號缺失!')])
    status = BooleanField(validators=[InputRequired(message='請選擇狀態!')])


class IncomeDataForm(BaseForm):
    form_id = StringField(validators=[Length(1, 7, message='製單流水號不可超過7個字元'),
                                      InputRequired(message='請輸入製單流水號!')])
    uniform_num = StringField(validators=[Length(1, 8, message='申報單位統一編號不可超過8個字元'),
                                          InputRequired(message='請輸入申報單位統一編號')])
    id_no = StringField(validators=[Length(1, 12, message='所得人代號不可超過12個字元'),
                                    InputRequired(message='請輸入所得人代號!')])
    # id_num = StringField(validators=[Length(1, 10, message='所得人統一編(證)號不可超過10個字元'),
    #                                  InputRequired(message='請輸入所得人統一編(證)號!')])
    # id_name = StringField(validators=[Length(1, 50, message='所得人姓名不可超過50個字元'),
    #                                   InputRequired(message='請輸入所得人姓名!')])
    income_yyy = StringField(validators=[Length(1, 3, message='所得給付年度不可超過3個字元'),
                                         InputRequired(message='請輸入所得給付年度!')])
    income_mm = StringField(validators=[Length(1, 2, message='所得給付月份不可超過2個字元'),
                                        InputRequired(message='請輸入所得給付月份')])
    income_format = StringField(validators=[Length(1, 10, message='所得格式不可超過10個字元'),
                                            InputRequired(message='請輸入所得格式!')])
    income_mark = StringField(validators=[Length(0, 10, message='所得註記不可超過10個字元')])
    income_amt = IntegerField(validators=[InputRequired(message='請輸入給付總額')])
    tax_amt = IntegerField(validators=[InputRequired(message='請輸入扣繳稅額')])
    net_amt = IntegerField(validators=[InputRequired(message='請輸入給付淨額')])
    exe_industry = StringField(validators=[Length(0, 10, message='執行業務者業別不可超過10個字元')])
    other_income = StringField(validators=[Length(0, 10, message='其他所得給付項目帶號不可超過10個字元')])
    royalties_exp = StringField(validators=[Length(0, 10, message='稿費必要費用別不可超過10個字元')])
    house_tax_num = StringField(validators=[Length(0, 20, message='房屋稅籍邊號不可超過20個字元')])
    house_address = StringField(validators=[Length(0, 200, message='房屋坐落不可過200個字元')])
    declare_status = BooleanField(validators=[InputRequired(message='請選擇是否已是申報狀態!')])
    # comm_flag = BooleanField(validators=[InputRequired(message='請選擇是否為佣金轉入!')])
    # comm_id = IntegerField()
    remark = StringField(validators=[Length(0, 200, message='所得人備註不可超過200個字元')])