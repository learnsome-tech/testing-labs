# m02l03-03 · Watching the scopes fire

**Lesson:** [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) (lesson 2.3, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

In the lesson: Two tests, each asking for both fixtures. Run with output capturing turned off, which is what the dash s flag does, so the prints reach the screen instead of being swallowed and shown only on failure. Read the order. The price list is loaded once, before the first test. The basket is built twice, once per test. Nobody wrote a setup method, nobody wrote a tear down, and the tests themselves say nothing about construction: they name what they need and get it, at the frequency their scope demands.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/conftest.py`](starter/conftest.py)
- [`starter/test_scope.py`](starter/test_scope.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-03/starter`
2. Read `test_scope.py`.
3. Run it: `python3 -m pytest -q -s test_scope.py`.
4. Check it from the repository root: `./check m02l03-03`.

## Expected output

```text
loading the price list
building a basket
.building a basket
.
2 passed in 0.00s
```

## How to check

`./check m02l03-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q -s test_scope.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
