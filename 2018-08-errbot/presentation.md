---
marp: true
---

# Errbot

## Contents

* [Errbot framework presentation](#errbot-framework-presentation)
* [Making a simple bot](#making-a-simple-bot)
* [A journey in the source code](#a-journey-in-the-source-code)

## Errbot framework presentation

> Errbot is a chatbot, a daemon that connects to your favorite chat service and brings your tools into the conversation.

### Supported backends

* Slack
* Hangouts
* Telegram
* Discord
* Skype
* And many more! See [full list](http://errbot.io/en/latest/features.html#multiple-server-backends).

### Basic interactions

* Invite the bot to a room or private conversation.
* Interact with it:
    - `@mention` it.
    - `!command`s.
    - Automatic responses on certain keywords/regexes/events.

### Admin interactions

* Manage plugins (install/uninstall/browse/reload).
* Configure/manage the Errbot server.
* Run individual plugins' admin commands.

### Other features

* Webhooks (webserver)
* Dynamic plugins
* Scheduling (CRON-like)
* Extensible: everything is a plugin
    - Backends
    - Commands
    - Storage
* Great documentation!

## Making a Simple Bot

Example: [Rando](https://github.com/samueldg/err-rando)

Need two files:

* `*.plug` - Descriptor
* `*.py` - Python code

Just derive from [`BotPlugin`](http://errbot.io/en/latest/user_guide/plugin_development/basics.html#anatomy-of-a-botplugin)

## A journey in the source code

In this next section, we'll dive into nice Python standard library or language features that are exemplified by cool Errbot features.

### Container types

* Feature: [Bot plugin persistence](http://errbot.io/en/latest/user_guide/plugin_development/persistence.html?highlight=self%5B#how-to-use-it)
* Description: Classes that walk like a `dict` and quack like a `dict`.
* Demo: [demo_container_type.py](./code/demos/demo_container_type.py)
* In Errbot's source code: [errbot/storage/__init__.py#StoreMixin](https://github.com/errbotio/errbot/blob/e0f93c7eef41fadbf3c6cc3793df55987c33bd79/errbot/storage/__init__.py#L20)

### Standard library: `shelve`

* Feature: [Bot plugin persistence](http://errbot.io/en/latest/user_guide/plugin_development/persistence.html?highlight=self%5B#how-to-use-it)
* Description: Simple persistent key-value store for Python objects.
* Demo: [demo_shelve.py](./code/demos/demo_shelve.py)
* In Errbot's source code: [errbot/storage/shelf.py#ShelfStorage](https://github.com/errbotio/errbot/blob/95bb61f0118d598b11937758b473bc2943eba7a4/errbot/storage/shelf.py#L13)

### Decorators and function attributes

* Feature: [`@botcmd`](http://errbot.io/en/latest/user_guide/plugin_development/basics.html#anatomy-of-a-botplugin) decorator to register commands.
* Description: Register or mark functions or methods inside a class.
* Demo: [demo_decorators.py](./code/demos/demo_decorators.py)
* In Errbot's source code: [errbot/__init__.py#_tag_botcmd](https://github.com/errbotio/errbot/blob/95bb61f0118d598b11937758b473bc2943eba7a4/errbot/__init__.py#L63)

### Standard library: `difflib`

* Feature:

    > sam [11:07 PM]
    > !plugin reboad something
    >
    > errbot APP [11:07 PM]
    > Command "plugin" / "plugin reboad" not found.
    > Did you mean "!status plugins" or "!plugin reload" or "!plugin blacklist" or "!plugin config" ?

* Description: Easily get the closest matches given a string and a list of targets.
* Demo: [demo_difflib.py](./code/demos/demo_difflib.py)
* In Errbot's source code: [errbot/core.py#Errbot.unknown_command](https://github.com/errbotio/errbot/blob/21c282356892596cf18b356cfe2435c4abe41b70/errbot/core.py#L472)

### Standard library: `importlib`

* Feature: Dynamic plugin discovery and reloading.
* How to dynamically load/reload Python module?
* Demo: [demo_importlib.py](./code/demos/demo_difflib.py)
* In Errbot's source code: [errbot/plugin_manager.py#BotPluginManager.reload_plugin_by_name](https://github.com/errbotio/errbot/blob/6aaf2c5a81634d56430c93c72d659e9cead59d99/errbot/plugin_manager.py#L172)

## References

* [Errbot](http://errbot.io/en/latest/)
* [Errbot on GitHub](https://github.com/errbotio/errbot/)
* [Errbot plugin directory](https://github.com/errbotio/errbot/wiki)
* [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
* [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
* [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
* [Python Data Model: Emulating container types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types) (`__getitem__`, `__setitem__`, `__delitem__`)
* [PEP 318 — Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
