from exts import db
from datetime import datetime


class ListvalueModel(db.Model):
    __tablename__ = 'mc_value_set_all'
    set_value_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_type = db.Column(db.String(30), nullable=False)
    value_code = db.Column(db.String(10), nullable=True)
    value_name = db.Column(db.String(100), nullable=False)
    value_desc = db.Column(db.String(200), nullable=True)
    parent_value = db.Column(db.String(10), nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    creation_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creater = db.relationship("MCUser", foreign_keys=[creation_by], backref='clistvalues')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='ulastvalues')


class ReportBasicInformModel(db.Model):
    __tablename__ = 'mc_register_all'
    register_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uniform_num = db.Column(db.String(8), nullable=False, unique=True)
    site_name = db.Column(db.String(30), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    creation_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creater = db.relationship("MCUser", foreign_keys=[creation_by], backref='cregisters')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='uregisters')


class EarnerBasicInformModel(db.Model):
    __tablename__ = 'mc_id_set_all'
    id_no = db.Column(db.String(12), nullable=False, primary_key=True)
    id_num = db.Column(db.String(10), nullable=False, unique=True)
    id_name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(10), nullable=False)
    id_type = db.Column(db.String(1), nullable=False)  # A-境內居住者, B-非境內居住者
    id_value_code = db.Column(db.String(10), nullable=False)
    id_value_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    tel = db.Column(db.String(20), nullable=True)
    id_mark = db.Column(db.String(10), nullable=False)
    remark = db.Column(db.String(200), nullable=True)
    status = db.Column(db.BOOLEAN, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    creation_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creater = db.relationship("MCUser", foreign_keys=[creation_by], backref='cearners')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='uearners')


class IncomeModel(db.Model):
    __tablename__ = "mc_income_all"
    form_id = db.Column(db.String(7), nullable=False, primary_key=True)
    uniform_num = db.Column(db.String(8), db.ForeignKey("mc_register_all.uniform_num"), nullable=False)
    id_no = db.Column(db.String(12), db.ForeignKey("mc_id_set_all.id_no"), nullable=False)
    id_num = db.Column(db.String(10), db.ForeignKey("mc_id_set_all.id_num"), nullable=False)
    id_name = db.Column(db.String(50), nullable=False)
    income_yyy = db.Column(db.String(3), nullable=False)
    income_mm = db.Column(db.String(2), nullable=False)
    income_format = db.Column(db.String(10), nullable=False)
    income_mark = db.Column(db.String(10), nullable=True)
    income_amt = db.Column(db.Integer, nullable=False, default=0)
    tax_amt = db.Column(db.Integer, nullable=False, default=0)
    net_amt = db.Column(db.Integer, nullable=False, default=0)
    exe_industry = db.Column(db.String(10), nullable=True)
    other_income = db.Column(db.String(10), nullable=True)
    royalties_exp = db.Column(db.String(10), nullable=True)
    house_tax_num = db.Column(db.String(20), nullable=True)
    house_address = db.Column(db.String(200), nullable=True)
    declare_status = db.Column(db.BOOLEAN, nullable=False)
    comm_flag = db.Column(db.BOOLEAN, nullable=False, default=True)
    comm_id = db.Column(db.Integer, db.ForeignKey("mc_comm_all.comm_id"), nullable=True)
    remark = db.Column(db.String(200), nullable=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    creation_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creater = db.relationship("MCUser", foreign_keys=[creation_by], backref='cincomes')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='uincomes')


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











