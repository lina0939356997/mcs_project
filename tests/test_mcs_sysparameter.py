# get sysparameters的畫面
def test_mcs_sysparameters(auth_client):
    url = "/sysparameters/"
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url