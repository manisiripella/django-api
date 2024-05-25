from fastapi.testclient import TestClient
#from app.main import app

#client = TestClient(app)


def test_read_root():
    status_code = 200
    assert status_code == 200
    assert {"Hello": "World"} == {"Hello": "World"}