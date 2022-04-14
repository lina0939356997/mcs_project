from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, DataRequired
from ..forms import BaseForm


class AddRegisterForm(BaseForm):
    uniform_num = StringField(validators=[Length(8, 8, message='統一編號為8個字元'),
                                          InputRequired(message='請輸入統一編號')])
    site_name = StringField(validators=[Length(1, 30, message='單位名稱不可超過30個字元'),
                                        InputRequired(message='請輸入單位名稱')])


class UpdateRegisterForm(AddRegisterForm):
    register_id = IntegerField(validators=[InputRequired(message='id缺失!')])


class AddEarnerForm(BaseForm):
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
    status = SelectField('狀態', choices=[('Y', 'Y'), ('N', 'N')]
                             , validators=[DataRequired(message='請輸入狀態！')], coerce=str)


class UpdateEarnerForm(AddEarnerForm):
    id_id = IntegerField(validators=[InputRequired(message='id缺失!')])


class SwitchEarnerForm(BaseForm):
    id_id = IntegerField(validators=[InputRequired(message='id缺失!')])
    status = SelectField('狀態', choices=[('Y', 'Y'), ('N', 'N')]
                             , validators=[DataRequired(message='請輸入狀態！')], coerce=str)


class AddIncomeForm(BaseForm):
    form_no = StringField(validators=[Length(1, 7, message='製單流水號不可超過7個字元'),
                                      InputRequired(message='請輸入製單流水號!')])
    uniform_num = StringField(validators=[Length(1, 8, message='申報單位統一編號不可超過8個字元'),
                                          InputRequired(message='請輸入申報單位統一編號')])
    id_no = StringField(validators=[Length(1, 12, message='所得人代號不可超過12個字元'),
                                    InputRequired(message='請輸入所得人代號!')])
    yyy = StringField(validators=[Length(1, 3, message='所得給付年度不可超過3個字元'),
                                  InputRequired(message='請輸入所得給付年度!')])
    mm = StringField(validators=[Length(1, 2, message='所得給付月份不可超過2個字元'),
                                 InputRequired(message='請輸入所得給付月份')])
    format = StringField(validators=[Length(1, 10, message='所得格式不可超過10個字元'),
                                     InputRequired(message='請輸入所得格式!')])
    mark = StringField(validators=[Length(0, 10, message='所得註記不可超過10個字元')])
    amt = IntegerField(validators=[InputRequired(message='請輸入給付總額')])
    tax_amt = IntegerField(validators=[InputRequired(message='請輸入扣繳稅額')])
    net_amt = IntegerField(validators=[InputRequired(message='請輸入給付淨額')])
    exe_industry = StringField(validators=[Length(0, 10, message='執行業務者業別不可超過10個字元')])
    other_income = StringField(validators=[Length(0, 10, message='其他所得給付項目帶號不可超過10個字元')])
    roya_exp = StringField(validators=[Length(0, 10, message='稿費必要費用別不可超過10個字元')])
    house_tax = StringField(validators=[Length(0, 20, message='房屋稅籍邊號不可超過20個字元')])
    house_add = StringField(validators=[Length(0, 200, message='房屋坐落不可過200個字元')])
    decl_status = SelectField('狀態', choices=[('Y', 'Y'), ('N', 'N')]
                                  , validators=[DataRequired(message='請輸入狀態！')], coerce=str)
    pay_id = IntegerField()
    remark = StringField(validators=[Length(0, 200, message='所得人備註不可超過200個字元')])


class UpdateIncomeForm(AddIncomeForm):
    form_id = IntegerField(validators=[InputRequired(message='id缺失!')])
