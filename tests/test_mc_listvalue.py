from apps.mc.models import ValueSetModel
from sqlalchemy import text
from tests import engine

# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_mc_listvalues_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from value_set where value_name like :s"),
                     {"s": "%test%"}
                     )


# get listvalues的畫面
def test_mc_listvalues(auth_client):
    url = "/listvalues/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_mc_alistvalue(auth_client):
    mock_request_data = {
        "set_type": "所得代碼",
        "value_code": "T",
        "value_name": "test",
        "value_desc": "這是測試",
        "parent_value": "50",
    }
    url = "/alistvalue/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        listvalue = ValueSetModel.query.filter_by(value_name="test").first()
        assert listvalue.set_value_id is not None


# 修改
def test_mc_ulistvalue(auth_client):
    listvalue = ValueSetModel.query.filter_by(value_name="test").first()
    mock_request_data = {
        "set_value_id": listvalue.set_value_id,
        "set_type": "所得代碼2",
        "value_code": "U",
        "value_name": "test2",
        "value_desc": "這是測試2",
        "parent_value": "51",
    }
    url = "/ulistvalue/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        listvalue = ValueSetModel.query.filter_by(value_name="test2").first()
        assert listvalue.set_value_id is not None

    # 刪除
    listvalue = ValueSetModel.query.filter_by(value_name="test2").first()
    mock_request_data = {
        "set_value_id": listvalue.set_value_id,
    }
    url = "/dlistvalue/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
