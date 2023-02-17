# Pytest Training

Baseline:

```bash
python -m unittest tests/test_00_unittest.py
```

Pytest is compatible! And has better output

```bash
pytest tests/test_00_unittest.py
```

From now on, I'll be using `-v` (`--verbose`) so the output is clearer.

```bash
pytest -v tests/test_00_unittest.py
```

First convert the simplest test to a function:

```bash
pytest -v tests/test_01_function.py
```

`self.assertRaises` -> `pytest.raises`

```bash
pytest -v tests/test_02_raises.py
```

Multiple tests in one:

```bash
pytest -v tests/test_03_parametrization.py
```

Add fixture:

```bash
pytest -v tests/test_04_fixtures.py
```

What if I don't want this to load every time?

```bash
pytest -v tests/test_05_fixture_scopes.py
```

Wait, why am I not seeing the `print()` output?

```bash
pytest -v -s tests/test_05_fixture_scopes.py
# Go back and edit the scope! Add: (scope='module')
pytest -v -s tests/test_05_fixture_scopes.py
```

What if I need some cleanup?

```bash
pytest -v -s tests/test_06_fixture_context.py
```

Builtin fixtures:

```bash
pytest -v -s tests/test_07_builtin_fixtures.py
# Get the full list: 
pytest --fixtures
```

```bash
pytest -v -s tests/test_08_expected_failures.py
# Go fix the bug!
pytest -v -s tests/test_08_expected_failures.py
```

## CLI options

We've seen `-s`, `-v`, `--fixtures`. What else!

```bash
pytest --help
```

Woah!

Pattern match:

```bash
pytest -v tests/test_04_fixtures.py -k test_get_second_element_for_sho
```

Marks:

```bash
pytest -v tests/test_09_custom_marks.py  -m fast
pytest -v tests/test_09_custom_marks.py  -m slow
```

Others:

* `--pdb`: Jump in debugger on error.
* `--lf, --last-failed` rerun only the tests that failed at the last run (or all if none failed)

## Doctests

```bash
pytest -v tests/test_10_doctest.py
pytest -v --doctest-modules=the_code tests/test_10_doctest.py
```

## Plugins

### Pytest xdist

```bash
pytest -v -n 4
```

### Pytest Coverage

```bash
pytest --cov=the_code --cov-report=html && open htmlcov/index.html
```

## Other topics

* Sharing fixtures in `conftest.py`
* Meaningful error messages through assertion inspection.
    - Can even define your own!
* Indirect fixture parametrization
* Use fixtures from other fixtures
    - E.g. You need an API client to your server, which requires a running server
* Auto-use fixtures
