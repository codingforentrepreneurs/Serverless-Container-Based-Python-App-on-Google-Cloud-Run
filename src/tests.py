from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)

def test_get_home_status():
    path = "/"
    # python requests
    # r = requests.get(path)
    response = client.get(path)
    status_code = response.status_code
    content_type = response.headers['content-type']
    assert status_code == 200 # HTTP response
    assert content_type == "application/json"
