from exts import db


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











