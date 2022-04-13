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
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creator = db.relationship("MCUser", foreign_keys=[created_by], backref='ccomms')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='ucomms')


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
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("mc_user_all.account"), nullable=False)

    creator = db.relationship("MCUser", foreign_keys=[created_by], backref='ccommlines')
    updater = db.relationship("MCUser", foreign_keys=[updated_by], backref='ucommlines')