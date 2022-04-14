import config
from apps.models import ReportBasicInformModel
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_mcs_basicinforms_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_register_all where uniform_num like :s"),
                     {"s": "%test%"}
                     )


# get reportinforms的畫面
def test_mcs_reportinforms(auth_client):
    url = "/reportinforms/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_mc_areportinform(auth_client):
    mock_request_data = {
        "uniform_num": "test0000",
        "site_name": "測試組織"
    }
    url = "/areportinform/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        reportinform = ReportBasicInformModel.query.filter_by(uniform_num="test0000").first()
        assert reportinform.register_id is not None


# 修改
def test_mc_ureportinform(auth_client):
    reportinform = ReportBasicInformModel.query.filter_by(uniform_num="test0000").first()
    mock_request_data = {
        "register_id": reportinform.register_id,
        "uniform_num": "test1111",
        "site_name": "測試組織2"
    }
    url = "/ureportinform/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        reportinform = ReportBasicInformModel.query.filter_by(uniform_num="test1111").first()
        assert reportinform.register_id is not None


def test_mcs_basicinformsend_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_register_all where uniform_num like :s"),
                     {"s": "%test%"}
                     )
