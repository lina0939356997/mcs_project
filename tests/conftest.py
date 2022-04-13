import pytest

import config
from app import create_app
from apps.mc.models import MCUser


@pytest.fixture()
def app():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    app.config.update({
        "TESTING": True,
    })
    app.app_context().push()
    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def auth_client(client):
    with client.session_transaction() as session:
        role = MCUser.query.filter_by(permission='admin').first()
        session[config.MC_USER_ID] = role.user_id
    yield client


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
