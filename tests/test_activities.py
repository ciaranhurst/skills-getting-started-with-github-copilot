from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_names = set(activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert set(response.json()) == expected_names
    assert len(expected_names) == 9


def test_get_activities_returns_expected_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    for details in response.json().values():
        assert expected_fields <= set(details)


def test_get_activities_includes_seeded_participants(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()[activity_name]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]
