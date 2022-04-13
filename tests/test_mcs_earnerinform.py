import config
from apps.models import EarnerBasicInformModel
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_mcs_earnerinforms_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_id_set_all where id_no like :s"),
                     {"s": "%test%"}
                     )


# get earnerinforms的畫面
def test_mcs_earnerinforms(auth_client):
    url = "/earnerinforms/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_mc_aearnerinform(auth_client):
    mock_request_data = {
        "id_no": "test",
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
        "status": True,
    }
    url = "/aearnerinform/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earnerinform = EarnerBasicInformModel.query.filter_by(id_num="T000").first()
        assert earnerinform.id_no is not None


# 修改
def test_mc_uearnerinform(auth_client):
    earnerinform = EarnerBasicInformModel.query.filter_by(id_no="test").first()
    mock_request_data = {
        "id_no": earnerinform.id_no,
        "id_num": "T111",
        "id_name": "測試人員2",
        "phone_num": "0987654321",
        "id_type": "B",
        "id_value_code": "所得人為非本國人",
        "id_value_name": "所得人為非本國人",
        "address": "",
        "tel": "",
        "id_mark": "測試員2",
        "remark": "測試2",
        "status": False,
    }
    url = "/uearnerinform/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earnerinform = EarnerBasicInformModel.query.filter_by(id_num="T111").first()
        assert earnerinform.id_no is not None


# 切換狀態
def test_mc_searnerinform(auth_client):
    earnerinform = EarnerBasicInformModel.query.filter_by(id_num="T111").first()
    mock_request_data = {
        "id_no": earnerinform.id_no
    }
    url = "/searnerinform/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        earnerinform = EarnerBasicInformModel.query.filter_by(id_num="T111", status=True).first()
        assert earnerinform.id_no is not None


def test_mcs_earnerinformsend_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_id_set_all where id_no like :s"),
                     {"s": "%test%"}
                     )
