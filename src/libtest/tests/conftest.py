import pytest

@pytest.fixture
def test_fixture():
    return "test fixture"

@pytest.fixture
def another_test_fixture():
    return "another test fixture"
