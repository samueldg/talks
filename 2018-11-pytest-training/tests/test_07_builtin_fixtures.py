"""Showcasing some builtin fixtures.
"""

import logging

from the_code import second_element


def print_true_nature():
    print("I'm a teapot")


def test_capsys(capsys):
    print_true_nature()
    captured = capsys.readouterr()
    assert "pot" in captured.out
    assert captured.err == ""


def test_caplog(caplog):
    caplog.set_level(logging.DEBUG)
    second_element([0, 1])  # Don't care about the result.

    assert len(caplog.records) == 2

    for record in caplog.records:
        assert record.levelno == logging.DEBUG
        assert record.levelname == "DEBUG"  # Alternative

    assert "About to get an element" in caplog.text
