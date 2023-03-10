from fastapi.testclient import TestClient

from currywurst_service.main import app

client = TestClient(app)


def test_get_currywurst_hello():
    response = client.get("v1/currywurst/hello")
    assert response.status_code == 200

def test_post_currywurst_purchase_failing_validation():
    response = client.post(
        "v1/currywurst/pay",
        json={
            "eur_inserted": 10,
        },
    )

    assert response.status_code == 422