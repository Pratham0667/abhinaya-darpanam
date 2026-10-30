def test_list_mudras_endpoint(client):
    response = client.get("/api/mudras")
    assert response.status_code == 200
    assert "mudras" in response.get_json()


def test_unknown_mudra_returns_404(client):
    response = client.get("/api/mudras/999")
    assert response.status_code == 404
