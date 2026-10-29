def test_mudra_list_api(client):
    response = client.get("/api/mudras")
    assert response.status_code == 200
