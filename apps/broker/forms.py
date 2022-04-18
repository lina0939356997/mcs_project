from wtforms import StringField, IntegerField, FloatField, SelectField, DateTimeField
from wtforms.validators import InputRequired, Length
from ..forms import BaseForm


class AddBrokerForm(BaseForm):
    broker_name = StringField(validators=[Length(1, 50, message="導遊名稱不可超過50個字元"), InputRequired(
        message="請輸入導遊名稱")])
    broker_num = StringField(validators=[Length(1, 10, message="導遊編號不可超過10個字元"), InputRequired(
        message="請輸入導遊編號")])
    travel = StringField(validators=[Length(1, 50, message="旅行社名稱不可超過50個字元"), InputRequired(
        message="請輸入旅行社名稱")])
    phone = StringField(validators=[Length(1, 10, message="手機號碼不可超過10個字元"), InputRequired(
        message="請輸入手機號碼")])
    address = StringField(validators=[Length(0, 200, message="地址不可超過200個字元")])


class UpdateBrokerForm(AddBrokerForm):
    broker_id = IntegerField(validators=[InputRequired(message="id缺失！")])


class TakeComm(BaseForm):
    order_num = StringField(validators=[Length(1, 30, message='訂單編號不可超過30個字元'), InputRequired(
        message='請輸入訂單編號')])
    group_name = StringField(validators=[Length(1, 50, message='團體名稱不可超過50個字元'), InputRequired(
        message='請輸入團體名稱')])
    car = DateTimeField(validators=[Length(0, 30, message='車次名稱不可超過30個字元')])
    order_date = StringField(validators=[InputRequired(message='請輸入訂單日期')])
    broker_id = IntegerField(validators=[InputRequired(message='請輸入導遊編號')])


# class AddComm(TakeComm):
#     sale_amt = IntegerField(validators=[IntegerField(message='請輸入銷售總額')])
#     rate = FloatField(validators=[IntegerField(message='請輸入佣金比率')])
#     comm_amt = IntegerField(validators=[IntegerField(message='請輸入佣金總額')])
#     comm_type = StringField(validators=[Length(1, 30, message='佣金型態不可超過30個字元'), IntegerField(
#         message='請輸入佣金型態')])
#     cal_type = StringField(validators=[Length(1, 30, message='計算型態不可超過30個字元'), IntegerField(
#         message='請輸入計算型態')])
#     status = StringField(validators=[Length(1, 20, message='狀態不可超過20個字元'), IntegerField(
#         message='請輸入狀態')])

