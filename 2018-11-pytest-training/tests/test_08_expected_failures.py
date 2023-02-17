import pytest

from the_code import third_element


@pytest.mark.skip(reason="This test always sucked")
def test_please_skip_this():
    return 'four' / 'two'


@pytest.mark.xfail(strict=True)
def test_get_third_element_strict_xfail():
    assert third_element(['a', 'b', 'c']) == 'c'


@pytest.mark.xfail(strict=False)
def test_get_third_element_lax_xfail():
    assert third_element(['a', 'b', 'c']) == 'c'
