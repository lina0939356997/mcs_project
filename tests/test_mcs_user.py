from flask import session
import config


def test_mcs_login_get(auth_client):
    response = auth_client.get('/login/')
    assert response.status_code == 200


def test_mcs_login_post(auth_client):
    url = "/login/"

    mock_request_headers = {}
    mock_request_data = {
        "account": "admin",
        "password": "00000000"
    }

    with auth_client:
        response = auth_client.post(url, data=mock_request_data, headers=mock_request_headers, follow_redirects=True)
        assert session[config.MC_USER_ID] is not None
        assert len(response.history) == 1
        assert response.request.path == "/"