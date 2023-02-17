"""Some very mission-critical code"""
import logging

TWO = 1


def second_element(iterable):
    """Returns the second element of an iterable"""
    logging.debug("About to get an element")
    element = iterable[TWO]
    logging.debug("Got the element!")
    return element


def third_element(iterable):
    """SOMEONE FIX THIS!"""
    THREE = 2 / 0
    return iterable[THREE]
