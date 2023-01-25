"""Demo of the standard library's `shelve` module.

We simply create a shelve and store/retrieve different Python data types.
"""

import datetime
import os.path
import shelve


DB_FILENAME = 'persistence.db'
CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_FILEPATH = os.path.join(CURRENT_DIR_PATH, DB_FILENAME)

with shelve.open(DB_FILEPATH) as store:
    store['string'] = 'Hello!'
    store['now'] = datetime.datetime.utcnow()
    store['int'] = 1337
    store['null'] = None
    store['dict'] = {
        "a": 1.337,
    }

print(f'Shelve stored: {DB_FILEPATH}')

with shelve.open(DB_FILEPATH) as store:
    for key, value in store.items():
        print(f"{key} => {value} ({type(value)})")
    store['string'] = 'Hello!'
    store['now'] = datetime.datetime.utcnow()
    store['int'] = 1337
    store['null'] = None
    store['dict'] = {
        "a": 1.337,
    }

