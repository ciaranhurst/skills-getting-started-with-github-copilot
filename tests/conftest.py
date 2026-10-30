"""Shared fixtures for the backend API tests.

Tests in this suite follow the Arrange-Act-Assert pattern: each test body is
three blocks marked with `# Arrange`, `# Act` and `# Assert`, with exactly one
client call in the Act block.
"""

import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    snapshot = copy.deepcopy(activities)
    yield
    # Restore in place so the handlers keep seeing the same dict object.
    activities.clear()
    activities.update(snapshot)
