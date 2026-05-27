from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_names = set(activities.keys())

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload.keys()) == expected_activity_names


def test_get_activities_returns_expected_activity_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for activity_data in payload.values():
        assert set(activity_data.keys()) == expected_keys
        assert isinstance(activity_data["participants"], list)
        assert isinstance(activity_data["max_participants"], int)
