from exts import db
from app import create_app
from apps.broker import models as broker_models
from apps.mc import models as mc_models

BrokerModel = broker_models.BrokerModel
UserModel = mc_models.UserModel


def load_seeds():
    '''
    載入seed data，寫入資料庫
    全部寫入之後再commit
    '''
    for i, row in enumerate(open("seeds/user.csv", encoding="utf-8")):
        row = row.rstrip()
        account, password, name, permission, created_at, created_by, updated_at, updated_by = row.split(",")
        user = UserModel(account=account, password=password, name=name, permission=permission, created_at
                         =created_at, created_by=created_by, updated_at=updated_at, updated_by=updated_by)
        db.session.add(user)
    for i, row in enumerate(open("seeds/broker.csv", encoding="utf-8")):
        row = row.rstrip()
        broker_name, broker_num, travel, phone, address, created_at, created_by, updated_at, updated_by = row.split(",")
        broker = BrokerModel(broker_name=broker_name, broker_num=broker_num, travel=travel, phone=phone, address
                             =address, created_at=created_at, created_by=created_by, updated_at=updated_at, updated_by
                             =updated_by)
        db.session.add(broker)

    db.session.commit()
    return True


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    result = load_seeds()
    if result:
        print("Load seed data successful!")
