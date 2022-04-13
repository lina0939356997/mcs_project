import config
from apps.models import IncomeModel
from sqlalchemy import text
from tests import engine


# 刪除測試資料，以避免過去測試過程中產生的垃圾資料影響測試
def test_mcs_incomedatas_clean():
    with engine.connect() as conn:
        conn.execute(text("delete from mc_income_all where form_id like :s"),
                     {"s": "%test%"}
                     )


# get incomedatas的畫面
def test_mcs_incomedatas(auth_client):
    url = "/incomedatas/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


# 新增
def test_mc_aincomedata(auth_client):
    mock_request_data = {
        "form_id": "test",
        "uniform_num": "12345678",
        "id_no": "E11111",
        # "id_num": "A1234",
        # "id_name": "測試者1",
        "income_yyy": "111",
        "income_mm": "04",
        "income_format": "所得格式1",
        "income_mark": "所得註記1",
        "income_amt": 1000,
        "tax_amt": 100,
        "net_amt": 900,
        "exe_industry": "執行業務者業別1",
        "other_income": "代號1",
        "royalties_exp": "稿費必要費用別1",
        "house_tax_num": "房屋稅及編號1",
        "house_address": "房屋坐落",
        "declare_status": True,
        # "comm_flag": True,
        "remark": "所得人備註",
    }
    url = "/aincomedata/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        incomedata = IncomeModel.query.filter_by(form_id="test").first()
        assert incomedata.form_id is not None


# 修改
def test_mc_uincomedata(auth_client):
    incomedata = IncomeModel.query.filter_by(form_id="test").first()
    mock_request_data = {
        "form_id": "test",
        "uniform_num": "87654321",
        "id_no": "F22222",
        # "id_num": "B4321",
        # "id_name": "測試者2",
        "income_yyy": "110",
        "income_mm": "03",
        "income_format": "所得格式2",
        "income_mark": "0",
        "income_amt": 2000,
        "tax_amt": 200,
        "net_amt": 1800,
        "exe_industry": "",
        "other_income": "",
        "royalties_exp": "",
        "house_tax_num": "",
        "house_address": "",
        "declare_status": True,
        # "comm_flag": True,
        # "comm_id": 1,
        "remark": "",
    }
    url = "/uincomedata/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
        incomedata = IncomeModel.query.filter_by(income_format="所得格式2").first()
        assert incomedata.form_id is not None

    # 刪除
    incomedata = IncomeModel.query.filter_by(form_id="test").first()
    mock_request_data = {
        "form_id": incomedata.form_id,
    }
    url = "/dincomedata/"
    with auth_client:
        response = auth_client.post(url, data=mock_request_data)
        assert response.status_code == 200
