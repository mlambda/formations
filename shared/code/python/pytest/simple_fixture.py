import pytest


@pytest.fixture
def integers():
    return [(2, 2), (21, 21)]


def add(a, b):
    return a + b


def test_add(integers):
    for a, b in integers:
        assert add(a, b) == add(b, a)
