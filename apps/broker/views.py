from flask import Blueprint, render_template
from exts import scheduler

bp = Blueprint("broker", __name__, url_prefix='/broker')


# @bp.route("/")
# def add_job():
#     job1 = scheduler.add_job(
#         func=calculate_comm(),
#         trigger="interval",
#         seconds=30,
#         id="insert_comm",
#         name="insert_comm",
#         replace_existing=True,
#     ),
#
#     job2 = scheduler.add_job(
#         func=post_comm(),
#         trigger="interval",
#         seconds=30,
#         id="show_kanban",
#         name="show_kanban",
#         replace_existing=True,
#     )
#     context = post_comm()
#     return render_template("kanban/kanbans.html", **context)
#
# @bp.route("/pause/")
# def pause_job():
#     job = scheduler.pause_job(id="comm_instant")
#     return "%s pause!" % job
#
#
# @bp.route("/resume/")
# def resume_job():
#     job = scheduler.resume_job(id="comm_instant")
#     return "%s resume!" % job
