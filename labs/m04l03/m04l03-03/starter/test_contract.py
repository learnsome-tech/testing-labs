def test_profile_contract():
    response = {"id": "u seven", "name": "Ada"}

    assert response["id"]
    assert response["name"] == "Ada"
