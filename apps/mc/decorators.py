from flask import session, redirect, url_for, g
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.MC_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('mc.login'))
    return inner
