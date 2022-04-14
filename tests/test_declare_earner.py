from apps.declare.models import IdSetModel
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_declare_earners_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from id_set where id_no like :s"),
                     {"s": "%test%"}
                     )


# get earners的畫面
def test_declare_earners(auth_client):
    url = "/declare/earners/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_declare_aearner(auth_client):
    mock_request_data = {
        "id_no": "test0",
        "id_num": "T000",
        "id_name": "測試人員",
        "phone_num": "0912345678",
        "id_type": "A",
        "id_value_code": "所得人為本國人",
        "id_value_name": "所得人為本國人",
        "address": "測試地址",
        "tel": "057777777",
        "id_mark": "測試員",
        "remark": "測試",
        "status": "Y",
    }
    url = "/declare/aearner/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earner = IdSetModel.query.filter_by(id_no="test0").first()
        assert earner.id_id is not None


# 修改
def test_declare_uearner(auth_client):
    earner = IdSetModel.query.filter_by(id_no="test0").first()
    mock_request_data = {
        "id_id": earner.id_id,
        "id_no": "test1",
        "id_num": "T111",
        "id_name": "測試人員2",
        "phone_num": "0987654321",
        "id_type": "B",
        "id_value_code": "所得人為非本國人",
        "id_value_name": "所得人為非本國人",
        "address": "",
        "tel": "",
        "id_mark": "測試員2",
        "remark": "",
        "status": "N",
    }
    url = "/declare/uearner/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earner = IdSetModel.query.filter_by(id_no="test1").first()
        assert earner.id_id is not None


# 切換狀態
def test_declare_searner(auth_client):
    earner = IdSetModel.query.filter_by(id_no="test1").first()
    mock_request_data = {
        "id_id": earner.id_id
    }
    url = "/declare/searner/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earner = IdSetModel.query.filter_by(id_no="test1", status="Y").first()
        assert earner.id_id is not None


def test_mcs_earner_clean_end():
    with engine.connect() as conn:
        conn.execute(text("delete from id_set where id_no like :s"),
                     {"s": "%test%"}
                     )
