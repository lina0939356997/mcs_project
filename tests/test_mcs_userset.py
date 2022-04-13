import config
from apps.mc.models import MCUser
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_mcs_usersets_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_user_all where account like :s"),
                     {"s": "%test%"}
                     )


# get usersets的畫面
def test_mcs_usersets(auth_client):
    url = "/usersets/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_mc_auserset(auth_client):
    mock_request_data = {
        "account": "test",
        "password": "11111111",
        "name": "test",
        "permission": "admin"
    }
    url = "/auserset/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        userset = MCUser.query.filter_by(account="test").first()
        assert userset.user_id is not None


# 修改
def test_mc_uuserset(auth_client):
    userset = MCUser.query.filter_by(account="test").first()
    mock_request_data = {
        "user_id": userset.user_id,
        "account": "test2",
        "password": "22222222",
        "name": "test2",
        "permission": "user"
    }
    url = "/uuserset/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        userset = MCUser.query.filter_by(account="test2").first()
        assert userset.user_id is not None

    # 刪除
    userset = MCUser.query.filter_by(account="test2").first()
    mock_request_data = {
        "user_id": userset.user_id,
    }
    url = "/duserset/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
