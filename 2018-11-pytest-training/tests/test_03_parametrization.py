import pytest

from the_code import second_element


def test_get_second_element_from_list():
    my_list = ['red', 'green', 'blue']
    assert second_element(my_list) == 'green'


@pytest.mark.parametrize('iterable', [
    [],  # Empty
    [':('],  # Too short (1 element)
])
def test_get_second_element_for_short_list(iterable):
    with pytest.raises(IndexError):
        second_element(iterable)
