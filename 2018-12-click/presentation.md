---
marp: true
---

# Click

---

## Contents

* [Why Click?](#why-click)
* [Features](#features)
* [References](#references)

---

## Why Click?

---

### What is Click?

> Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.
>
> It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

Source: Click project page

---

### Why a CLI?

* Give a flexible, powerful and discoverable interface to your code.
* Can be used both interactively or via scripting.
* Can be composed with other tools (e.g. `grep`, `xargs`, etc.)
* :heart:ed by power users.

---

### Why not `sys.argv`?

* Makes code harder to reason about.
* Only handles positional arguments.
    - Which in turn makes your CLI harder to use.
* Need to handle parameter validation yourself.
    - Or show some really esoteric tracebacks to the user.
* It's 2018!

---

### Why not `argparse`?

* Not particulary easy to use, a lot of boilerplate.
* Hard to nest/compose commands.
* Auto-generated help: meh!
* Click has tons of additional goodies.
* Plus, it's by Armin Ronacher([@mitsuhiko](https://github.com/mitsuhiko)), the author of [Flask](http://flask.pocoo.org/).

---

## Features

---

### Commands

The command is the basic concept in Click. It is a function that you can run from the command line.

Examples:

* `top`
* `ps`
* `clear`

The recommended use is to decorate the function with `@click.command`. Calling the decorated function (typically from an `if __name__ == '__main__'` block) turns your Python module in a CLI!

Note: For now, we will always call our scripts with `python file_path.py`, but it's possible to declare executable names like `pip`, `pipenv`, `ipython`, etc.

---

### Arguments (positional)

Arguments are to your command what positional args are to your Python function. They are passed without a name, and their order determines how they are used.

Examples:

* `ls some_dir/`
* `cp some_file.txt some_dir/`

Those are declared via the `@click.argument()` decorator. Click will match the argument name with the parameter in your Python function.

---

### Variadic arguments

Variadic positional arguments take an arbitrary amount of values. As a user, you are passing a list of values, rather than a single value.

Examples:

* `git add debug.log sandstorm.mp3 meme.jpg`
* `cp debug.log sandstorm.mp3 meme.jpg some_dir/`
    - Note the subtle difference!

Passing `nargs=-1` to `click.argument()` will make your argument variadic. Note that there can only be one, for a given command.

Tip: Try to support the case with 0 arguments. Your robot users and `*`-globbers will thank you!

---

### Options (named)

Options are to your command what kwargs are to your Python function. They are passed with a name/alias.

* Not required, by default.
* Can be a boolean flag or not

Examples:

* `git add --patch debug.log sandstorm.mp3 meme.jpg`
* `docker run -d -p 80:8080 --volume $PWD:/home my_image`

Those are declared via the `@click.option()` decorator. Click will match the option name with the parameter in your Python function.

Note: This is the most featureful component in Click. If you read one thing from the documentation, it should be [Options](http://click.palletsprojects.com/en/7.x/options/).

---

### Builtin types

* `click.STRING`
* `click.INT` / `click.IntRange`
* `click.FLOAT` / `click.FloatRange`
* `click.BOOL`
* `click.UUID`
* `click.Choice`
* `click.DateTime`

---

### File types

* Use `click.File` (or weaker `click.Path`).
* Allow the Unix-y `-`for `stdin` or `stdout`.
* Will fail early if the path doesn't exist, but should.
* Can lazily open the file for writing, only when needed.
* Can make atomic changes to a file (only swap at the end).

---

### Custom types and validation

> Custom parameter types can be implemented by subclassing `click.ParamType`.

You just need to define:

* A name;
* A `convert` method that takes a string, and returns a value, or raises a validation error.

---

### Commands groups, a.k.a. subcommands

Subcommands allow you to have different functionality within a single command entrypoint.

Examples:

* `git [commit|clone|push|...]`
* `pip [install|uninstall|freeze|...]`

Arbitrary nesting is also conceivable:

* `gcloud components install ...`
* `kubectl config current-context`

This can be achieved via the `click.group` decorator or `click.Group` class.

---

### Input prompts

* Passing `prompt=True` to `click.option` means that if the value is missing, it will be prompted.
* `hide_input=True` can also be used to make what the user typed invisible in the console, which is useful for passwords.
* You can also `click.prompt()` or `click.confirm()` at any point during the execution.

---

### Console output

`click.echo`: a better version of `print()`:

* Handles unicode errors in the terminal
* Works with Python 2 and 3.
* Handles ANSI color codes, and proper formatting.

`click.style` allows you to format the output text (color, bold, blinking, underline).

`click.secho` == combination of `click.echo` with `click.style`.

---

### Testing

The `click.testing` module enables you to easily test your CLI, including the input and output.

* You can test commands and subcommands with arbitrary parameters.
* You can specify anything in the execution context (environment variables, terminal width, etc.)
* An isolated file system is available, to test input/output without side-effects.
* You can also emulate prompts.

---

### And more!

* Bash completion.
* Dynamic command nesting and composition.
* Passing values through environment variables.
* Progress bars.
* Launching your editor (cf. `git commit`)
* Using setuptools to have an executable entrypoint.

---

## Conclusion

* Use Click!
* The [docs](https://click.palletsprojects.com) are awesome!

---

## References

* [Click documentation](https://click.palletsprojects.com)
* [Click on GitHub](https://github.com/pallets/click)
* [`argparse` - Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)
* [Armin Ronacher's blog](http://lucumr.pocoo.org/) - Tangentially related, but awesome.

---

## Questions?
