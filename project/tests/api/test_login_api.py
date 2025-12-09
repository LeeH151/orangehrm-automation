from project.api.auth_api import AuthAPI


def test_api_login():
    api = AuthAPI()
    resp = api.login()
    # If login returns JSON with access_token
    if hasattr(resp, 'json'):
        data = resp.json()
    else:
        data = resp

    assert resp is not None