from wtforms import StringField, IntegerField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, DataRequired
from ..forms import BaseForm


class LoginForm(BaseForm):
    account = StringField(validators=[Length(1, 20, message='帳號不可超過20個字元'), InputRequired(message='請輸入帳號!')])
    password = StringField(validators=[Length(8, 10, message='密碼介於8~10個字元'), InputRequired(message='請輸入密碼!')])


class AddUsersetForm(BaseForm):
    account = StringField(validators=[Length(1, 20, message='帳號不可超過20個字元'), InputRequired(message='請輸入帳號！')])
    password = StringField(validators=[Length(8, 10, message='密碼介於8~10個字元'), InputRequired(message='請輸入密碼！')])
    name = StringField(validators=[Length(1, 20, message='姓名不可超過20個字元'), InputRequired(message='請輸入姓名！')])
    permission = SelectField('權限', choices=[('admin', 'admin'), ('user', 'user')]
                             , validators=[DataRequired(message='請輸入權限等級！')], coerce=str)


class UpdateUsersetForm(AddUsersetForm):
    user_id = IntegerField(validators=[InputRequired(message='ID缺失！')])


class AddListvalueForm(BaseForm):
    set_type = StringField(validators=[Length(1, 30, message='清單類別值不可超過30個字元'),
                                       InputRequired(message='請輸入清單值類別!')])
    value_code = StringField(validators=[Length(0, 10, message='清單值代碼不可超過10個字元')])
    value_name = StringField(validators=[Length(1, 100, message='清單值不可超過100個字元'),
                                         InputRequired(message='請輸入清單值!')])
    value_desc = StringField(validators=[Length(1, 200, message='清單值描述不可超過200個字元'),
                                         InputRequired(message='請描述清單值!')])
    parent_value = StringField(validators=[Length(0, 10, message='ParentValue不可超過10個字元')])


class UpdateListvalueForm(AddListvalueForm):
    set_value_id = IntegerField(validators=[InputRequired(message='id缺失!')])
