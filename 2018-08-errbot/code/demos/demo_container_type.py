"""Here we implement a blockchain, append-only ledger of a python dictionary.

All mutations to the internal state are stored in a text file,
as a new JSON-encoded line.

ICO scheduled early 2019.
"""

import json
import os.path


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
BLOCKCHAIN_FILENAME = 'blockchain.txt'
BLOCKCHAIN_FILEPATH = os.path.join(CURRENT_DIR_PATH, BLOCKCHAIN_FILENAME)


class BlockchainKeyValueStore:

    def __init__(self):
        if not os.path.isfile(BLOCKCHAIN_FILEPATH):
            with open(BLOCKCHAIN_FILEPATH, 'w') as out_file:
                out_file.write(json.dumps({}) + '\n')

        with open(BLOCKCHAIN_FILEPATH) as in_file:
            self._dict = json.load(in_file)

    def __setitem__(self, key, value):
        self._dict[key] = value
        self.log()

    def __getitem__(self, key):
        return self._dict[key]

    def __delitem__(self, key):
        del self._dict[key]
        self.log()

    def log(self):
        with open(BLOCKCHAIN_FILEPATH, 'a') as out_file:
            out_file.write(json.dumps(self._dict) + '\n')
