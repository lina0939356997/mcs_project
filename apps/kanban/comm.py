from flask import render_template
from sqlalchemy import func
from exts import db
from ..models import PosViewModel, MCSCommModel, MCSCommLineModel


def calculate_comm():
    db.session.query(MCSCommLineModel).delete()
    db.session.query(MCSCommModel).delete()

    # MCSCommLineModel.delete()
    result = db.session.query(
        PosViewModel.order_num,
        PosViewModel.group_name,
        PosViewModel.car,
        PosViewModel.order_date,
        func.sum(PosViewModel.amt).label('subtotal')
    ).filter(PosViewModel.sale_line_id.isnot(None)) \
        .group_by(PosViewModel.order_num,
                  PosViewModel.group_name,
                  PosViewModel.car,
                  PosViewModel.order_date)\
        .all()

    for row in result:
        comm_id = None
        comm = MCSCommModel(order_num=row.order_num,
                            group_name=row.group_name,
                            car=row.car,
                            order_date=row.order_date,
                            sale_amt=row.subtotal
                            )
        db.session.add(comm)
        db.session.flush()
        comm_id = comm.comm_id
        try:
            result_line = db.session.query(PosViewModel).filter_by(car=row.car).all()
            for row_line in result_line:
                comm_line = MCSCommLineModel(
                    comm_id=comm_id,
                    sale_line_id=row_line.sale_line_id,
                    ticket=row_line.ticket,
                    sale_num=row_line.sale_num,
                    sale_line_num=row_line.sale_line_num,
                    item_no=row_line.item_no,
                    qty=row_line.qty,
                    amt=row_line.amt
                )
                db.session.add(comm_line)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            if comm_id is not None:
                db.session.rollback()
            return str(e)
    print("寫入comm、comm_line，成功!")
    return "寫入comm、comm_line，成功!"


def post_comm():
    query_obj = None
    query_obj = MCSCommModel.query.order_by(MCSCommModel.order_date.desc())
    kanbans = query_obj
    context = {
        'kanbans': kanbans
    }
    print("post_comm")
    return context

