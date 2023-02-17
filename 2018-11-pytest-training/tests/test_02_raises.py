import pytest

from the_code import second_element


def test_get_second_element_from_list():
    my_list = ["red", "green", "blue"]
    assert second_element(my_list) == "green"


def test_get_second_element_from_empty_list():
    with pytest.raises(IndexError):
        second_element([])
