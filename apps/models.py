from exts import db
from datetime import datetime


class BrokerCommmonModel(db.Model):
    __tablename__ = "mc_comm_all"
    comm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comm_name = db.Column(db.String(50), nullable=False)


class PosViewModel(db.Model):
    __bind_key__ = 'pos'
    __tablename__ = 'order_sale'
    sale_line_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_num = db.Column(db.String(30))
    order_date = db.Column(db.DateTime)
    group_name = db.Column(db.String(50))
    car = db.Column(db.String(30))
    ticket = db.Column(db.String(20))
    sale_num = db.Column(db.String(20))
    sale_line_num = db.Column(db.String(5))
    item_no = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    amt = db.Column(db.Integer)


class MCSCommModel(db.Model):
    __tablename__ = 'mcs_comm'
    comm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_num = db.Column(db.String(30), nullable=False)
    group_name = db.Column(db.String(50), nullable=False)
    car = db.Column(db.String(30), nullable=True)
    order_date = db.Column(db.DateTime, nullable=False)
    sale_amt = db.Column(db.Integer, nullable=False)


class MCSCommLineModel(db.Model):
    __tablename__ = 'mcs_comm_line'
    comm_line_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comm_id = db.Column(db.Integer, db.ForeignKey("mcs_comm.comm_id"), nullable=False)
    sale_line_id = db.Column(db.Integer, nullable=False)  # order_sale: sale_line_id
    ticket = db.Column(db.String(20), nullable=False)
    sale_num = db.Column(db.String(20), nullable=False)
    sale_line_num = db.Column(db.String(5), nullable=False)
    item_no = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=0)
    amt = db.Column(db.Integer, nullable=False, default=0)


# class PayModel(db.Model):
#     __tablename__ = 'pay'
#     pay_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     pay_date = db.Column(db.DateTime, nullable=False)
#     decl_type = db.Column(db.String(20), nullable=False)
#     broker_id = db.Column(db.Integer, db.ForeignKey("broker.broker_id"), nullable=True)
#     invoice_num = db.Column(db.String(10), nullable=True)
#     uniform_num = db.Column(db.String(8), nullable=True)
#     site_name = db.Column(db.String(50), nullable=True)
#     pay_status = db.Column(db.String(20), nullable=False, default="NEW")  # NEW/CLOSED/REVERSE
#     decl_status = db.Column(db.String(1), nullable=False, default="N")  # Y/N
#     total_amt = db.Column(db.Integer, nullable=False, )











