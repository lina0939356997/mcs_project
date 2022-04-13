from flask import Blueprint, render_template
from exts import scheduler
from tasks.mock_pos_syns import mock_pos

bp = Blueprint("mock_pos", __name__, url_prefix='/mock_pos')


@bp.route("/start/")
def add_job():
    """Add a task.
    :url: /add_task/
    :returns: job
    """
    job = scheduler.add_job(
        func=mock_pos,
        trigger="interval",
        seconds=10,
        id="mock_pos",
        name="mock_pos",
        replace_existing=True,
    )
    return render_template("kanban/kanbans.html")



@bp.route("/pause_job/")
def pause_job():
    job = scheduler.pause_job(id="pos_sync")
    return "%s pause!" % job


@bp.route("/resume_job/")
def resume_job():
    job = scheduler.resume_job(id="pos_sync")
    return "%s resume!" % job



