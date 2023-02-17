import json

import pytest

from the_code import second_element


@pytest.fixture(scope='module')
def alphabet():
    """Read alphabet file and return contents.

    Kinda verbose.
    """
    with open('tests/alphabet.json') as f:
        print('Loading JSON file')
        return json.load(f)


def test_get_second_element_in_alphabet(alphabet):
    assert second_element(alphabet) == 'b'


def test_element_is_in_original_iterable(alphabet):
    assert second_element(alphabet) in alphabet
