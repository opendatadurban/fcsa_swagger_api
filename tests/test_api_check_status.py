from starlette.testclient import TestClient
from api.status_checker.api_check_status import index

client = TestClient

# create the test class for main
def test_api_check_status():
    response = client.get("/status_checker")
    assert response.status_code == 200
    assert response.json() == {"Login": "Success"}

def test_get_session_id(new_sap):
    response = client.get("/session-id")
    assert response.status_code == 200
