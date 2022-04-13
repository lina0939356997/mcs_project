from flask import Blueprint, render_template
from .comm import calculate_comm, post_comm
from tasks.mock_pos_syns import mock_pos
from exts import scheduler
from utils import restful

bp = Blueprint("kanban", __name__, url_prefix='/kans')

@bp.route("/")
def kanbancontrol():
    return render_template("kanban/kanbancontrols.html")

@bp.route("/kanban/")
def kanban():
    context = post_comm()
    return render_template("kanban/kanbans.html", **context)


@bp.route("/startkanban/", methods=['POST'])
def add_job():
    job = scheduler.add_job(
        func=mock_pos,
        trigger="interval",
        seconds=30,
        id="mock_pos",
        name="mock_pos",
        replace_existing=True,
    )

    job1 = scheduler.add_job(
        func=calculate_comm,
        trigger="interval",
        seconds=30,
        id="insert_comm",
        name="insert_comm",
        replace_existing=True,
    ),
    print("排成開始")
    return restful.success()


@bp.route("/resumeinsert_comm/", methods=['POST'])
def resume_job():
    job = scheduler.resume_job(id="insert_comm")
    print("繼續抓資料")
    return restful.success()


@bp.route("/pauseinsert_comm/", methods=['POST'])
def pause_job():
    job = scheduler.pause_job(id="insert_comm")
    print("停止抓資料")
    return restful.success()


@bp.route("/resumemock_pos/", methods=['POST'])
def resume_job1():
    job1 = scheduler.resume_job(id="mock_pos")
    print("繼續新增資料")
    return restful.success()


@bp.route("/pausemock_pos/", methods=['POST'])
def pause_job1():
    job1 = scheduler.pause_job(id="mock_pos")
    print("停止新增資料")
    return restful.success()
