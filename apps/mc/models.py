from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    permission = db.Column(db.String(10), nullable=False)  # admin-管理者, user-一般使用者
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    created_by = db.Column(db.String(10), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_by = db.Column(db.String(10), nullable=False)


class ValueSetModel(db.Model):
    __tablename__ = 'value_set'
    set_value_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_type = db.Column(db.String(30), nullable=False)
    value_code = db.Column(db.String(10), nullable=True)
    value_name = db.Column(db.String(100), nullable=False)
    value_desc = db.Column(db.String(200), nullable=False)
    parent_value = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    created_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_by = db.Column(db.String(10), db.ForeignKey("user.account"), nullable=False)

    creator = db.relationship("UserModel", foreign_keys=[created_by], backref='clistvalues')
    updater = db.relationship("UserModel", foreign_keys=[updated_by], backref='ulastvalues')