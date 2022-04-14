from exts import db
from datetime import datetime


class CommModel(db.Model):
    __tablename__ = 'comm'
    comm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_num = db.Column(db.String(30), nullable=False)
    group_name = db.Column(db.String(50), nullable=False)
    car = db.Column(db.String(30), nullable=True)
    order_date = db.Column(db.DateTime, nullable=False)
    sale_amt = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    comm_amt = db.Column(db.Integer, nullable=False)
    comm_type = db.Column(db.String(30), nullable=False)
    cal_type = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='ccomms')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='ucomms')


class CommLineModel(db.Model):
    __tablename__ = 'comm_line'
    comm_line_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comm_id = db.Column(db.Integer, db.ForeignKey("comm.comm_id"), nullable=False)
    sale_line_id = db.Column(db.Integer, nullable=False)  # order_sale: sale_line_id
    ticket = db.Column(db.String(20), nullable=False)
    sale_num = db.Column(db.String(20), nullable=False)
    sale_line_num = db.Column(db.String(5), nullable=False)
    item_no = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=0)
    amt = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='ccommlines')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='ucommlines')


class BrokerModel(db.Model):
    __tablename__ = 'broker'
    broker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    broker_name = db.Column(db.String(50), nullable=False)
    broker_num = db.Column(db.String(10), nullable=False)
    travel = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cbrokers')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='ubrokers')


class CommBrokerModel(db.Model):
    __tablename__ = 'comm_broker'
    comm_broker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    broker_id = db.Column(db.Integer, db.ForeignKey("broker.broker_id"), nullable=False)
    comm_id = db.Column(db.Integer, db.ForeignKey("comm.comm_id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    broker = db.relationship("BrokerModel", foreign_keys=[broker_id], backref='comms')
    comm = db.relationship("CommModel", foreign_keys=[comm_id], backref='brokers')
    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='ccommbrokers')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='ucommbrokers')


class PayModel(db.Model):
    __tablename__ = 'pay'
    pay_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pay_date = db.Column(db.DateTime, nullable=False)
    decl_type = db.Column(db.String(20), nullable=False)
    broker_id = db.Column(db.Integer, db.ForeignKey("broker.broker_id"), nullable=True)
    invoice_num = db.Column(db.String(10), nullable=True)
    uniform_num = db.Column(db.String(8), nullable=True)
    site_name = db.Column(db.String(50), nullable=True)
    pay_status = db.Column(db.String(20), nullable=False, default='NEW')  # NEW/CLOSED/REVERSE
    decl_status = db.Column(db.String(1), nullable=False, default='N')  # Y/N
    total_amt = db.Column(db.Integer, nullable=False)
    tax_amt = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    broker = db.relationship("BrokerModel", foreign_keys=[broker_id], backref='incomes')
    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cpays')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='upays')


class PayLineModel(db.Model):
    __tablename__ = 'pay_line'
    pay_line_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pay_id = db.Column(db.Integer, db.ForeignKey("pay.pay_id"), nullable=False)
    comm_broker_id = db.Column(db.Integer, db.ForeignKey("comm_broker.comm_broker_id"), nullable=True)
    pay_type = db.Column(db.String(20), nullable=False)
    pay_amt = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    pay = db.relationship("PayModel", foreign_keys=[pay_id], backref='comm_brokers')
    comm_broker = db.relationship("CommBrokerModel", foreign_keys=[comm_broker_id], backref='pays')
    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cpaylines')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='upaylines')
