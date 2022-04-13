from exts import db


class MCUser(db.Model):
    __tablename__ = 'mc_user_all'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    permission = db.Column(db.String(10), nullable=False)  # admin-管理者, user-一般使用者
