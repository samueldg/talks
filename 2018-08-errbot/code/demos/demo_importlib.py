"""Demo of the standard library's `importlib` module.

Here we overwrite a stdlib module with some other file.
"""

import json
import os.path
from importlib import machinery


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OTHER_MODULE_NAME = "demo_container_type.py"
OTHER_MODULE_FILEPATH = os.path.join(CURRENT_DIR_PATH, OTHER_MODULE_NAME)


if __name__ == "__main__":

    print(dir(json))

    print("Black magic voodoo:")
    machinery.SourceFileLoader("json", OTHER_MODULE_FILEPATH).load_module("json")

    print(dir(json))
    print(json.BlockchainKeyValueStore)
