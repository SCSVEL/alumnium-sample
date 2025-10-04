import pytest

# You can add common fixtures here for all tests in the tests/ directory.

@pytest.fixture(scope="session")
def example_fixture():
    # Example fixture, replace or extend as needed
    return "This is a session-scoped fixture."
