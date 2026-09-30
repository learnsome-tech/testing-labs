# m02l01-03 · Running the suite

**Lesson:** [Introducing pytest](https://learnsome.tech/learn/testing-course/m02l01) (lesson 2.1, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write and run a pytest suite with no configuration, read the session header, and select tests by name from the command line.

In the lesson: Three tests. The first two assert an answer. The third one asserts that a bad call raises, using the raises context manager, which passes only if the block really raises that class of error. Run the whole file with no arguments and no configuration. Read the header: pytest tells you the platform, the interpreter, the root it worked out for itself, the plugins that are loaded, and how many tests it collected. Then a dot per passing test, and the count. That header is the first thing to read when a suite misbehaves on somebody else's machine.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_discount.py`](starter/test_discount.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `test_discount.py` the way the lesson builds it:
   - Lines 1–7: the first two assert
   - Lines 8–16: the third one
3. Run it: `python3 -m pytest test_discount.py`.
4. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
============================ test session starts =============================
platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/you/shop
plugins: cov-7.1.0
collected 3 items

test_discount.py ...                                                   [100%]

============================= 3 passed in 0.01s ==============================
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `python3 -m pytest test_discount.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
