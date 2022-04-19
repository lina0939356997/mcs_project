from .models import CommModel


def calculate_comm(comm_key: list, broker_id: int):
    print(comm_key)
    print(broker_id)


def select_broker_comm(broker_id: int):
    print(broker_id)
    query_obj = CommModel.query.filter_by(broker_id=broker_id).all()
    comms = query_obj
    return comms
