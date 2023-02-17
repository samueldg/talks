"""Now feature-complete!
"""

import json

import pytest

from the_code import second_element


def test_get_second_element_from_list():
    my_list = ["red", "green", "blue"]
    assert second_element(my_list) == "green"


@pytest.mark.parametrize(
    "iterable",
    [
        [],  # Empty
        [":("],  # Too short (1 element)
    ],
)
def test_get_second_element_for_short_list(iterable):
    with pytest.raises(IndexError):
        second_element(iterable)


@pytest.fixture
def alphabet():
    """Read alphabet file and return contents."""
    with open("tests/alphabet.json") as f:
        return json.load(f)


def test_get_second_element_in_alphabet(alphabet):
    assert second_element(alphabet) == "b"
