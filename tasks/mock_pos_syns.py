import datetime
import random
from exts import db
from apps.models import PosViewModel


def mock_pos():
    order_num = 1
    order_date = datetime.date.today()
    group_name = "佐登妮絲團"
    ticket = random.randint(1, 90)
    if ticket > 60:
        car = "丙車"
    elif ticket > 30:
        car = "乙車"
    else:
        car = "甲車"
    sale_num = random.randint(1, 1000)
    sale_line_num = random.randint(1, 1000)
    item_no = random.choice(["A", "B", "C", "D", "E", "F", "G"])
    qty = random.randint(1, 20)
    amt = random.randint(500, 3000)
    with db.app.app_context():
        pos = PosViewModel(order_num=order_num,
                           order_date=order_date,
                           group_name=group_name,
                           car=car,
                           ticket=ticket,
                           sale_num=sale_num,
                           sale_line_num=sale_line_num,
                           item_no=item_no,
                           qty=qty,
                           amt=amt)

        db.session.add(pos)
        db.session.commit()
        print("sync mock pos data successful!")


# def mock_pos():
#     order_id = random.randint(1, 10000)
#     item = random.choice(["九胜肽", "面膜", "精油", "乳液", "精華液", "乳霜", "洗髮精", "沐浴乳", "洗手液"])
#     qty = random.randint(1, 20)
#     subtotal = random.randint(500, 3000)
#     broker_id = random.randint(1, 10)
#     broker_name = "task"
#     broker_tel = "0925412412"
#     order_date = datetime.date.today()
#     with db.app.app_context():
#         pos = PosViewModel(order_id=order_id,
#                            order_date=order_date,
#                            item=item,
#                            qty=qty,
#                            subtotal=subtotal,
#                            broker_id=broker_id,
#                            broker_name=broker_name,
#                            broker_tel=broker_tel)
#
#         db.session.add(pos)
#         db.session.commit()
#         print("sync mock pos data successful!")

