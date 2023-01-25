# Asynchronous Programming in Python

## Contents

* [Concurrency Options](#concurrency-options)
* [Asynchronous IO in Python](#asynchronous-io-in-python)
* [Example: Nuance API Client](#example-nuance-api-client)
* [Some Asynchronous IO Features in Python](#some-asynchronous-io-features-in-python)

## Concurrency Options

* Multithreading.
    - :-1: GIL.
* Multiprocessing
    - :-1: Overhead.
* Asynchronous IO
    - :-1: Only appropriate for IO-bound workloads.

## Asynchronous IO in Python

### Python 2

* [asyncore](https://docs.python.org/2/library/asyncore.html) (standard lib)
* [twisted](https://twistedmatrix.com/trac/)
* [tornado](http://www.tornadoweb.org/en/stable/)

### Python 3

* [tulip](http://code.google.com/p/tulip/) --> [asyncio](https://docs.python.org/3/library/asyncio.html) (standard lib since 3.4)
* `async`/`await` (syntax since Python 3.5)
* [aio-libs](https://github.com/aio-libs) ([aiohttp](https://aiohttp.readthedocs.io/en/stable/), [aioredis](https://aioredis.readthedocs.io/en/stable/), [aiopg](https://aiopg.readthedocs.io/en/stable/), etc.)
* [sanic](http://sanic.readthedocs.io/en/latest/)
* [curio](https://curio.readthedocs.io/en/latest/)
* [trio](https://trio.readthedocs.io/en/latest/)
* [uvloop](https://github.com/MagicStack/uvloop)

### `asyncio Overview

* One event loop calling callbacks.
* We want to maximize the use of a single thread.
* When doing nothing, the loop is not "busy-looping". It uses OS primitives (SELECT, EPOLL, etc.) to be smart about what callback to call next.
* You can spawn subprocesses.
* There are built-in primitives:
    - [Synchronization](https://docs.python.org/3/library/asyncio-sync.html#synchronization-primitives)
    - [Queue](https://docs.python.org/3/library/asyncio-queue.html)

## Example: Nuance API Client

Nuance Mix / NCS runtime sample application.

### General Architecture

![general-architecture](./images/general-architecture.png)

### Client Architecture

![client-architecture](./images/client-architecture.png)

## Some Asynchronous IO Features in Python

### `async`/`await`

* Since Python 3.5.
* More readable than `yield from`
* Allows using coroutines with generators more easily.

### `asyncio.Queue

* Async equivalent of [`queue.Queue`](https://docs.python.org/3.6/library/queue.html#queue.Queue).
* Has awaitable and non-awaitable access:
    - `get`/`put`
    - `get_nowait`/`put_nowait`

### `asyncio.ensure_future

* Schedule something, and wrap in a `Future`.
* Accepts any awaitable object.

### `__aiter__`

Define an iterable where you can call coroutines.

See for instance the [aiohttp WebSocket server](https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets).

```python
ws = web.WebSocketResponse()
await ws.prepare(request)
async for msg in ws:
    # Do stuff
```

### `__aenter__`/`__aexit__`

Define a context manager where entering and exiting can `await`.

See for instance the [aiohttp HTTP lient](https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request).

```python
async with aiohttp.ClientSession() as session:
    # Do stuff, don't care about freeing resources!
```

## Further Resources

* [Thinking in coroutines (Ĺukasz Langa, PyCon 2016)](https://www.youtube.com/watch?v=l4Nn-y9ktd4)
* [async/await and asyncio in Python 3.6 and beyond - (Yury Selivanov, PyCon 2017)](https://www.youtube.com/watch?v=2ZFFv-wZ8_g)
