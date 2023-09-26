---
marp: true
---

# Async Standup learnings

[samueldg/async-standups](https://github.com/samueldg/async-standups)

> This tool helps you write, publish, and keep track of your async standup reports.
>
> The standup data will be saved and manipulated in YAML files, and published to Slack in Markdown format.

-----

## Demo time!

-----

## What I learned

* Library usage
    - Jinja 2
    - Slackclient
    - Click
* Project setup
    - setuptools (`setup.py`)
    - Pipenv
* An invaluable life lesson

-----

### [Jinja2](http://jinja.pocoo.org/) templating

Jinja == f-strings on steroids

> Jinja is Beautiful
>
> -- Jinja Docs

-----

Pass data via a context namespace (here, only `sections`):

```txt
{%- for section_name, section_items in sections.items() if section_items%}
{{ section_name|title }}:
    {%- for section_item in section_items %}
- [{{ section_item.projects|join('/') }}] {{ section_item.action }}
    {%- endfor %}
{% endfor -%}
```

Then render the template!

-----

You have access to:

* Conditional logic
* Loops
* Directives (uppercase, escape, etc.)
    - Create your own, too.

Great for generating documents from structured data!

-----

### Slack API

You can impersonate yourself!

```python
from slackclient import SlackClient

API_TOKEN = 'SECRET_STUFF'
slack = SlackClient(API_TOKEN)
slack.api_call(
    'chat.postMessage',
    channel='comms-internal',
    text='Hello!',
    as_user=True,  # <-- Oh yeah!
)
```

-----

### Click

Recap?

See [technical training on Click](https://github.com/samueldg/talks/tree/master/2018-12-click)

-----

#### `--dry-run` option

IRL example:

```sh
# See what gitignore'd files you could delete
git clean -X --dry-run
```

DIY:

```python
@click.command()
@click.option('--dry-run', '-n', is_flag=True, default=False)
def publish(dry_run):
    ...
    if dry_run:
        print(f'#{channel}\n{rendered_text}')
    else:
        slack.api_call(...)
```

-----

#### Open a file in the editor

IRL example:

```sh
# Open your commit message in your editor
git commit
```

DIY:

```python
@click.command()
@click.option('--edit', '-e', is_flag=True, default=False)
def copy(edit):
    ...
    if edit:
        click.edit(
            filename='test.yml',
            extension='.yml',
            editor='subl',
            require_save=True,
        )
```

-----

#### How to have an executable for your script?

Before:

```sh
python standup/main.py copy --edit
python -m standup.main copy --edit
```

What I want:

```sh
standup copy --edit
```

That's how we segue into...

-----

### setuptools/`setup.py`

-----

How to have an executable entrypoint for your script?

In `setup.py`:

```py
setup(
    ...,
    entry_points={
        'console_scripts': [
            'standup = standup.main:cli',
        ],
    },
)
```

Syntax: `command = path.to.your.module:function`

-----

Behind the hood:

```sh
pipenv --venv
echo $VIRTUAL_ENV
echo $PATH
ls -l $VIRTUAL_ENV/bin
...
```

-----

#### How to include data in your package?

-----

To include non-Python files, you need:

* `include_package_data=True` in `setup()`
* `MANIFEST.in`

Examples:

* Templates
* Documentation
* Config files
* Sample data
* etc.

-----

#### How to include the version?

What I want:

1. This code:

    ```python
    >>> import standup
    >>> standup.__version__
    '0.0.1'
    ```

2. `version=...` in `setup()`
3. Version defined in only one place.

-----

**Problem**

You can't `import` your package... because it's not been set up.

**Solution**

```python
with open('standup/__init__.py') as f:
    # Not importing the file in setup.py!
    VERSION = re.search(r"__version__ = '(?P<version>.*?)'", f.read()).group('version')
```

It's [what Flask does](https://github.com/pallets/flask/blob/2c68f86336dc8729f58e8e19af0f49c269c1cfaa/setup.py#L12)!

-----

### Pipenv

How to have your dependencies installed with `pipenv install`, but also when you install the lib directly from `pip`, or from another package's dependencies?

In `setup.py`:

```python
REQUIREMENTS = [
    'click~=7.0',
    ...
]
```

In `Pipfile`:

```toml
[packages]
standup = {editable = true,path = "."}
```

-----

## Conclusion

Over-engineer stuff sometimes!
