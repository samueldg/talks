"""Demo of the standard library's `difflib` module.

We check a bunch of erroneous names against a list of valid names,
and determine the closest match.
"""

import difflib


VALID_NAMES = [
    "bruno",
    "kristin",
    "mo",
    "sam",
]

BAD_NAMES = [
    "kirtsin",
    "san",
    "pruno",
    "mooo",
]


if __name__ == "__main__":

    for bad_name in BAD_NAMES:

        closest_matches = difflib.get_close_matches(bad_name, VALID_NAMES)[0]
        print(f"{bad_name} => {closest_matches}")
