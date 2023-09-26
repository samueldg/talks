# Technical training: Python modules & packages

---

## What we'll cover

* What are modules and packages?
* What happens when we import and install one?
* Overview of the package management ecosystem and tools.
* Things you need to know when developing your own package.

Bonus:

* Miscellaneous Python trivia in the examples. :snake:

---

## Why we care?

Modular code is:

* Reusable
* Simpler
* Easier to maintain
* Scoped and namespaced

> Namespaces are one honking great idea  let's do more of those!
> 
> – Zen of Python

---
## What are modules and packages?

---

Noob Sam:

> A module is a Python file (?)

Python glossary:

> An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

---

Interestingly, a module can be written in C (e.g. `io`, `re`, `itertools`, etc.)

```python
>>> import functools
>>> import inspect
>>> functools.lru_cache
<function lru_cache at 0x10b6119d8>
>>> functools.reduce
<built-in function reduce>
>>> functools.lru_cache.__code__
???
>>> functools.reduce.__code__
???
>>> print(inspect.getsource(functools.lru_cache))
???
>>> print(inspect.getsource(functools.reduce))
???
```

---

`inspect.getsource`:

```python
>>> print(inspect.getsource(inspect.getsource))
def getsource(object):
    """Return the text of the source code for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    OSError is raised if the source code cannot be retrieved."""
    lines, lnum = getsourcelines(object)
    return ''.join(lines)
```

![yo-dawg](https://pbs.twimg.com/profile_images/2941650637/b75a4d9a7a4af01d936e91c77cd6083d.jpeg)

---

Noob Sam:

> A package is a directory with an `__init__.py` file (?)

Python Glossary:

> A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute.

---

We can tell which is not a package using this `__path__` attribute:

```python
>>> import http
>>> import http.client
>>> http.__file__
'/usr/local/lib/python3.7/http/__init__.py'
>>> http.__path__
['/usr/local/lib/python3.7/http']
>>> http.client.__file__
'/usr/local/lib/python3.7/http/client.py'
>>> http.client.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'http.client' has no attribute '__path__'
```

---

And now those error messages make more sense:

```
>>> import http.woot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'http.woot'
>>> import http.client.woot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'http.client.woot'; 'http.client' is not a package
```

---

### Wat?

```python
>>> import http
>>> http.client
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'http' has no attribute 'client'
>>> import http.client
```

* Attribute access: Only names defined in the `*.py` file for a regular module and `__init__.py` for a package module.
* Submodule access: Looks through the folder structure. 

---

### Wat? (cont'd)

```python
>>> import my_package
>>> my_package.sub
"I'm a constant!"
>>> import my_package.sub
>>> my_package.sub.wat
"I'm another constant!"
```

* Nothing prevents you from having a local variable and a submodule sharing the same name.
    - Don't do this!

---

## What happens when you `import` a module?

1. Interpreter searches for the module.
2. Module is executed, the result of which is a namespace.
3. This namespace is bound to a local name (in `locals`).


```python
>>> from pprint import pprint
>>> pprint(locals())
???
>>> import statistics
>>> pprint(locals())
???
>>> from statistics import *
>>> pprint(locals())
???
```

You can now:

* Access module's attributes by name (e.g. `module.attribute`)
* Pass the module around, as a first-class citizen (e.g. `print(module)`)

---

Useful-to-know implementation detail:

* `sys.modules` is where loaded modules are stored.
* It is updated **globally**, each module only imported once.

```python
>>> import sys
>>> sys.modules.keys()
???
>>> import inspect
>>> sys.modules.keys()
???
```

This guarantees initialization code and `atexit` hooks run only once.

---

## Tips

* Avoid `import *`, except when that's really what you want, or sometimes in sample code, for conciseness.

---

## Where does Python know where to search for modules?

1. Current directory
2. Anything you put in `$PYTHONPATH`
3. Multiple pre-defined paths (depends on the platform, the Python version, etc.)
    * Those will include the standard lib and user-installed packages.
    * Using virtualenvs ensure the isolation of these directories.

```python
>>> import sys
>>> sys.path
???
```

---

You can easily locate individual modules with `__file__`:

```python
>>> import os
>>> os.__file__
'/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'
>>> import tox
>>> tox.__file__
'/usr/local/lib/python3.7/site-packages/tox/__init__.py'
```
 
This can be useful to verify that you are loading the right code, look into the source code of a library, etc.
 
---

## Tips

* Don't manipulate `PYTHONPATH` or `sys.path` unless you really know what you're doing.
* Avoid name conflicts with standard lib modules.
    - Remember each module is loaded only once in `sys.modules`...

---

## What happens when you install a package?

Wouldn't it be nice to see what files are changed/added exactly when you `pip install` something?

If only we had some sort of process isolation technology with a file system that can easily be layered, and compared.

:thinking:

---

Docker to the rescue! :whale:


```sh
$ docker pull python:3.7-slim
$ docker run \
    --name py37-step1 \
    python:3.7-slim \
    pip install \
        chardet \
        --no-cache-dir \
        --disable-pip-version-check
$ docker commit py37-step1 py37-step1
$ docker run \
    --name py37-step2 \
    py37-step1 \
    pip install \
        six \
        --no-cache-dir \
        --disable-pip-version-check
```

---

And now, the prestige :tophat::

```
$ docker diff py37-step2
C /usr
C /usr/local
C /usr/local/lib
C /usr/local/lib/python3.7
C /usr/local/lib/python3.7/site-packages
C /usr/local/lib/python3.7/site-packages/__pycache__
A /usr/local/lib/python3.7/site-packages/__pycache__/six.cpython-37.pyc
A /usr/local/lib/python3.7/site-packages/six.py
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/METADATA
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/RECORD
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/WHEEL
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/top_level.txt
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/INSTALLER
A /usr/local/lib/python3.7/site-packages/six-1.12.0.dist-info/LICENSE
```

* :information_source: You cannot install multiple versions of the same package!

---

## `setup.py install` vs `develop`

* When running `setup.py install` or the default `pip install`,
a **copy** of the necessary source files will be added to your site-packages, available in the `sys.path` for further use.

* If running `setup.py develop` (or `pip install --editable`), a **symbolic link** will be created instead, meaning you can update your local files and have those changes reflected in the packages you import.

---

## Package management ecosystem and tools

---

## `setuptools`/`distutils`

`setuptools` is the lower-lever library responsible for packaging, distribution and installation of Python projects. If you install a Python package, it will be called.


`distutils` is an older alternative, that has been superseded but is still in the standard lib for legacy purposes.

---

## pip

Pip builds on top of `setuptools` and provides a means to download packages, manage installation, support packages in version control, etc. It also provides a friendlier experience with a CLI.

It is now shipped *de facto* with a lot of Python distributions.

---

## Pipenv

CLI tool that provides an improved UI on top of pip and virtualenvs.

Notable features:

* Dependency resolution and locking.
* Python versions management.
* Virtualenv management.
* Various other CLI utilities

---

## PyPI

* Stands for <u>Py</u>thon <u>P</u>ackage <u>I</u>ndex
* Public repository of Python packages, which Pip installs from by default.

---

## `setup.py`? `requirements.txt`? `Pipfile`?

* `Pipfile`: https://github.com/samueldg/async-standups/blob/f2deced69fec362b8554bae80b1ea07ad8f4cb63/Pipfile
* `setup.py`: https://github.com/samueldg/async-standups/blob/f2deced69fec362b8554bae80b1ea07ad8f4cb63/setup.py
* `requirements.txt`: https://github.com/xonsh/xonsh/blob/0.8.12/requirements-docs.txt

---

### When do I need a `setup.py`?

* If you want to build a library
    - Application vs. library
* If you want to have "console scripts"
    - E.g. `python make_predictions.py -n 3` -> `predict -n 3`
* If your code require extra steps (C extensions, platform checks, etc.)

---

## Also seen in the wild:

`setup.cfg`:

* (Optional) Way to provide arguments to `setup()` in a static config, rather than in Python code.

`MANIFEST.in`

* (Optional) Only useful when you need to declare additional, non-Python resources.
    - e.g. JSON config, Jinja templates, sample data files, etc.

---

## `__init__.py`

* Package initialization, define what's in the namespace.
* Add one, even if it's empty.

---

## `__all__`

* Restrict the names that are part of the module's namespace.

```python
# mypackage.py

json = {
    "delphia": {
        "is_cult": False
    }
}
IS_CULT = json["delphia"]["is_cult"]
```

```python
# myscript.py

>>> import json
>>> from mypackage import *
>>> IS_CULT
False
>>> json.dumps({})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'dumps'
```
---

## Tips

* `setup.py`should install your dependencies.
* Try `python setup.py sdist` then `pip install -e $PACKAGE` to test setup.
* Use package resources, when you need to refer to non-python files that are distributed with your library.
* Try using the library while NOT in the project directory (will help you catch path issues.)

---

## References

* https://docs.python.org/3/reference/import.html
* https://docs.python.org/3/glossary.html#term-package
* https://docs.python.org/3/glossary.html#term-module
* https://www.python.org/dev/peps/pep-0020/
* https://realpython.com/python-modules-packages/

* https://docs.python.org/3/library/inspect.html

* [pip](https://pip.pypa.io)
* [Pipenv](https://docs.pipenv.org)
* [setuptools](https://setuptools.readthedocs.io/en/latest/)
* [distutils](https://docs.python.org/3/distutils/index.html)
