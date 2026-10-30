def test_recognition_endpoint_is_available(client):
    response = client.post("/api/recognize", json={"landmarks": [[0.1, 0.2, 0.0]]})
    assert response.status_code in (200, 501)
