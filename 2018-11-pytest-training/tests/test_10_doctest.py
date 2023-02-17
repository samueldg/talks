import pytest


def reverse_list(iterable):
    """
    >>> reverse_list(['A', 'B'])
    ['B', 'A']
    """
    return list(reversed(iterable))


@pytest.fixture
def my_list():
    """Simple list."""
    return [1, 2, 3]


def test_reverse(my_list):
    assert reverse_list(my_list) == [3, 2, 1]
