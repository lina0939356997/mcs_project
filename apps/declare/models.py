from exts import db
from datetime import datetime


class RegisterModel(db.Model):
    __tablename__ = 'declare'
    register_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uniform_num = db.Column(db.String(8), nullable=False, unique=True)
    site_name = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cregisters')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='uregisters')


class EarnerModel(db.Model):
    __tablename__ = 'id_set'
    id_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_no = db.Column(db.String(12), nullable=False, unique=True)
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
    status = db.Column(db.String(1), nullable=False)  # Y/N
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cearners')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='uearners')


class IncomeModel(db.Model):
    __tablename__ = "income"
    form_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    form_no = db.Column(db.String(7), nullable=False, unique=True)
    uniform_num = db.Column(db.String(8), db.ForeignKey("declare.uniform_num"), nullable=False)
    id_no = db.Column(db.String(12), db.ForeignKey("id_set.id_no"), nullable=False)
    id_num = db.Column(db.String(10), db.ForeignKey("id_set.id_num"), nullable=False)
    id_name = db.Column(db.String(50), nullable=False)
    yyy = db.Column(db.String(3), nullable=False)
    mm = db.Column(db.String(2), nullable=False)
    format = db.Column(db.String(10), nullable=False)
    mark = db.Column(db.String(10), nullable=True)
    amt = db.Column(db.Integer, nullable=False, default=0)
    tax_amt = db.Column(db.Integer, nullable=False, default=0)
    net_amt = db.Column(db.Integer, nullable=False, default=0)
    exe_industry = db.Column(db.String(10), nullable=True)
    other_income = db.Column(db.String(10), nullable=True)
    roya_exp = db.Column(db.String(10), nullable=True)
    house_tax = db.Column(db.String(20), nullable=True)
    house_add = db.Column(db.String(200), nullable=True)
    decl_status = db.Column(db.BOOLEAN, nullable=False)
    pay_id = db.Column(db.Integer, db.ForeignKey("pay.pay_id"), nullable=True)
    remark = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    register_uniform = db.relationship("RegisterModel", foreign_keys=[uniform_num], backref='uniform_nums')
    earner_no = db.relationship("EarnerModel", foreign_keys=[id_no], backref='earner_nos')
    earner_num = db.relationship("EarnerModel", foreign_keys=[id_num], backref='earner_nums')
    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='cincomes')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='uincomes')