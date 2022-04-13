from exts import db
from app import create_app
from apps.mc import models as mc_models
from apps import models

MCUser = mc_models.MCUser
ReportBasicInform = models.ReportBasicInformModel
Earner = models.EarnerBasicInformModel
Common = models.BrokerCommmonModel


def load_seeds():
    '''
    載入seed data，寫入資料庫
    全部寫入之後再commit
    '''
    for i, row in enumerate(open("seeds/mc_user_all.csv", encoding="utf-8")):
        row = row.rstrip()
        account, password, name, permission = row.split(",")
        user = MCUser(account=account, password=password, name=name, permission=permission)
        db.session.add(user)

    for i, row in enumerate(open("seeds/mc_register_all.csv", encoding="utf-8")):
        row = row.rstrip()
        uniform_num, site_name, creation_date, creation_by, updated_date, updated_by = row.split(",")
        register = ReportBasicInform(uniform_num=uniform_num, site_name=site_name, creation_date=creation_date
                                     , creation_by=creation_by, updated_date=updated_date, updated_by=updated_by)
        db.session.add(register)

    for i, row in enumerate(open("seeds/mc_id_set_all.csv", encoding="utf-8")):
        row = row.rstrip()
        id_no, id_num, id_name, phone_num, id_type, id_value_code, id_value_name, address, tel, id_mark\
        , remark, status, creation_date, creation_by, updated_date, updated_by = row.split(",")
        earner = Earner(id_no=id_no, id_num=id_num, id_name=id_name, phone_num=phone_num, id_type=id_type, id_value_code
                        =id_value_code, id_value_name=id_value_name, address=address, tel=tel, id_mark
                        =id_mark, remark=remark, status=bool(status), creation_date=creation_date, creation_by
                        =creation_by, updated_date=updated_date, updated_by=updated_by)
        db.session.add(earner)

    for i, row in enumerate(open("seeds/mc_comm_all.csv", encoding="utf-8")):
        row = row.rstrip()
        comm_id, comm_name = row.split(",")
        comm = Common(comm_id=comm_id, comm_name=comm_name)
        db.session.add(comm)

    db.session.commit()
    return True


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    result = load_seeds()
    if result:
        print("Load seed data successful!")
