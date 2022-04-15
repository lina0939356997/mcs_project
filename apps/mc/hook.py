from .views import bp
import config
from flask import session, g
from .models import UserModel, ListvalueModel


@bp.before_request
def befoore_request():
    if config.MC_USER_ID in session:
        user_id = session.get(config.MC_USER_ID)
        user = UserModel.query.get(user_id)
        if user:
            g.user = user

