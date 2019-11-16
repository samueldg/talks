# Fantastic anti-patterns and where to find them: pinpointing performance bottlenecks :dragon:

-----

## The talk & takeaways

* Real-life case study
* Pinpoint performance bottlenecks with:
    - a sampling profiler
    - flame graphs :fire:
* Performance anti-patterns with remediation
* Neat features in Python's standard library :snake:

-----

## About me

* Samuel Dion-Girardeau
* Software engineer, linguist
* :heart: Python!
* Working at Delphia

-----

## Case study

* Crypto-assets trading backtesting program.
    - "How would strategy X perform?"
* Using the [catalyst](https://github.com/enigmampc/catalyst) algorithmic trading library.
* Prototype, need to be able to iterate fast!

-----

## Expected :pray:

```sh
python backtest.py --start=2016-01 --end=2018-01
```

Then:

* Get a coffee
* Wait ~5 minutes
* Output: "Your strategy made 10x profits :chart_with_upwards_trend:!"
	* Future crypto-millionaire :moneybag:

-----

## Actual :grimacing:

```sh
python backtest.py --start=2016-01 --end=2018-01
```

Then:

* Get a coffee
* Wait ~1 hour
* Coffee is cold
* Output: "You lost 90% of your starting capital :chart_with_downwards_trend:"
	* Future crypto-bankrupt :money_with_wings:

-----

## What's going on?

* Way too slow! Takes around an hour to run... :sleeping:
* Even when the strategy code isn't doing anything!
* How do we even go about troubleshooting this?
    - Print statements with timing?
* What if the bottleneck is in a third-party library?

----

# Solution: profiling, and flame graphs! :fire:

-----

## What is a profiler?

Program that analyses another program at runtime, and reports useful data, e.g. "what code was running".

Two major families:

* Instrumentation
* Sampling

-----

## Instrumentation

* Changes the target program with various hooks so it reports data
* Very accurate data points
* Costly
* Can affect the behaviour
* E.g. `coverage`

-----

## Sampling

* Statistical, so approximate
* Not costly (can run in prod!)
    - Some CPU/cache overhead
* No code changes, inspect a running program
* E.g. `py-spy`

  ```bash
  py-spy record \
         --pid 13337 \
         --function \
         --output flame_graph.svg \
         --duration 600 \
         --rate 1000
  ```
-----

## What are flame graphs?

* Visulization tools for profiler output.
* Gives a hierarchical representation of code paths and their relative sampling frequenecy.
* Can be interactive.

-----

## How do you read a flame graph?

----

![Flame graph example](assets/get_exchange_folder-after-zoomed.png)

* Vertical: Stack trace depth
* Horizontal axis: time spent, proportional to parent (:warning: no order)
* "Gaps" between vertical levels: time spent directly in the function

-----

## What to look for:

* Large horizontal portions
* Time spent in one function
* Recurring function calls

-----

# Performance anti-patterns + solutions

Back to case study (finally!)

-----

Result of running `py-spy`:

![Before redo fix](assets/redo-before.png)

-----

Zoom, enhance:

![Before redo fix (zoomed)](assets/redo-before-zoomed.png)

-----

## `redo.retry()` (simplified)

```python
def retry(action, args, kwargs, attempts=5):
    logging.debug(
        "calling %s with args: %s, kwargs: %s" % \
        (action.__name__, args, kwargs)
    )
    for i in attempts:
        try:
            action(*args, **kwargs)
        except:
            ... # Manage exceptions
        else:
            return
```

-----

### Anti-pattern: Costly eager string formatting

```python
    logging.debug(
        "calling %s with args: %s, kwargs: %s" % \
        (action.__name__, args, kwargs)
    )
```

#### `debug(msg, *args, **kwargs)`

> Logs a message with level `DEBUG` on this logger. The `msg` is the message format string, and the `args` are the arguments which are merged into msg using the string formatting operator. 
-----

### Solution: Lazy formatting in the `logging` standard library

```diff
     logging.debug(
-        "calling %s with args: %s, kwargs: %s" % \
-        (action.__name__, args, kwargs)
+        "calling %s with args: %s, kwargs: %s", \
+        action.__name__, args, kwargs,
     )
```

Saved ~10% of execution time!

-----

Result of running `py-spy` after that fix:

![After redo fix](assets/redo-after.png)


-----

What next?:

![Before get_exchange_folder fix](assets/get_exchange_folder-before.png)

-----

* `get_exchange_folder`, you say?
* `ensure_folder_exists`? Really?

-----

## `catalyst.get_exchange_folder()` (simplified)

```python
def get_exchange_folder(exchange_name):
    exchange_folder = os.path.join(
        DATA_ROOT, 'exchanges', exchange_name
    )
    ensure_directory(exchange_folder)
    return exchange_folder
```

* Called every hour in the simulation!

-----

### Anti-pattern: Repeated file system reads

* File system reads are expensive!
* Real life equivalent: `ensure_keyboard()`

-----

### Solution: `lru_cache` in the `functools` standard library

```diff
+from functools import lru_cache

+@lru_cache(maxsize=None)
 def get_exchange_folder(exchange_name):
     exchange_folder = os.path.join(
        DATA_ROOT, 'exchanges', exchange_name
     )
     ensure_directory(exchange_folder)
     return exchange_folder
```

Saved ~20% of execution time

-----

#### `@functools.lru_cache(maxsize=128, typed=False)`

> Decorator to wrap a function with a memoizing callable that saves up to the `maxsize` most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

-----


Result of running `py-spy` after both fixes:

![](assets/get_exchange_folder-after.png)

-----

Zoom, enhance:

![](assets/get_exchange_folder-after-zoomed.png)

* `retry`: Almost no overhead
* No more expensive folder check!

-----

## Conclusion: key takeaways

* Profilers are not scary
* Flame graphs are lit :fire:
* 30-35% improvements with two simple fixes!
* Led to improvements in [catalyst](https://github.com/enigmampc/catalyst) and [redo](https://github.com/mozilla-releng/redo)
* Read the py-spy docs, there is much more you can do with it, we barely scratched the surface!

-----

## Q & A

-----

## Links

* [Flame Graphs](http://www.brendangregg.com/flamegraphs.html)
* [Python Standarb Library: `logging`](https://docs.python.org/3/library/logging.html)
* [Python Standarb Library: `functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
* [benfred/py-spy](https://github.com/benfred/py-spy)
* [enigmampc/catalyst](https://github.com/enigmampc/catalyst)

Issues/PRs referenced:

* [mozilla-releng/redo#51](https://github.com/mozilla-releng/redo/pull/51)
* [enigmampc/catalyst#500](https://github.com/enigmampc/catalyst/issues/500)

Slides:

* [samueldg/talks](https://github.com/samueldg/talks)
