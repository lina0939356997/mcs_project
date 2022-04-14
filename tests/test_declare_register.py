from apps.declare.models import RegisterModel
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_declare_registers_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from register where uniform_num like :s"),
                     {"s": "%test%"}
                     )


# get registers的畫面
def test_declare_registers(auth_client):
    url = "/declare/registers/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_declare_aregister(auth_client):
    mock_request_data = {
        "uniform_num": "test0000",
        "site_name": "測試組織"
    }
    url = "/declare/aregister/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        register = RegisterModel.query.filter_by(uniform_num="test0000").first()
        assert register.register_id is not None


# 修改
def test_declare_uregister(auth_client):
    register = RegisterModel.query.filter_by(uniform_num="test0000").first()
    mock_request_data = {
        "register_id": register.register_id,
        "uniform_num": "test1111",
        "site_name": "測試組織2"
    }
    url = "/declare/uregister/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        register = RegisterModel.query.filter_by(uniform_num="test1111").first()
        assert register.register_id is not None


def test_declare_registers_end_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from register where uniform_num like :s"),
                     {"s": "%test%"}
                     )
