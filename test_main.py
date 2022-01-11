from fastapi.testclient import TestClient 

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.status_code != 500
    assert response.json() == {"message": "Hello World"}
    assert response.json() != {"message": "Hello world"}