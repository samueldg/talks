"""This code is executed by pytest at the beginning of the test run.

It allows us to import `the_code.py` in our tests, since this module is not
otherwise installed by a `setup.py`, for instance.
"""

import os
import sys


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, ROOT_DIR)
