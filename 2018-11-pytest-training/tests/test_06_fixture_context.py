import json

import pytest

from the_code import second_element


@pytest.fixture(scope="function")
def alphabet():
    """Read alphabet file and return contents.

    Even more verbose.
    """
    print("File not opened yet")
    with open("tests/alphabet.json") as f:
        print("File opened")
        yield json.load(f)
        print("File closed")


def test_get_second_element_in_alphabet(alphabet):
    print('Running "test_get_second_element_in_alphabet" ...')
    assert second_element(alphabet) == "b"


def test_element_is_in_original_iterable(alphabet):
    print('Running "test_element_is_in_original_iterable" ...')
    assert second_element(alphabet) in alphabet
