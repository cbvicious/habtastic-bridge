import pytest


@pytest.fixture
def numbers():
    a = 1
    b = 1
    return [a,b]


class TestApp:
    def test_addition(self, numbers):
        res = a + b
        assert res == 2
