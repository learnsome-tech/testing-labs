# m02l01-04 · Seeing every test by name

**Lesson:** [Introducing pytest](https://learnsome.tech/learn/testing-course/m02l01) (lesson 2.1, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write and run a pytest suite with no configuration, read the session header, and select tests by name from the command line.

In the lesson: Now ask for the verbose report, with the header suppressed to keep it on one screen. Instead of a dot per test you get the full identifier of each one: the file, a pair of colons, and the function name, followed by its verdict and the percentage of the run completed. That identifier is not decoration. It is an address: you can paste any one of those lines back onto the command line to run exactly that test and nothing else, which is what you will do fifty times while fixing a failure. The verbose report is also what continuous integration logs should carry, because a dot tells you nothing six weeks later.

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

1. Go to the starter: `cd labs/m02l01/m02l01-04/starter`
2. Read `test_discount.py`.
3. Run it: `python3 -m pytest -v --no-header test_discount.py`.
4. Check it from the repository root: `./check m02l01-04`.

## Expected output

```text
============================ test session starts =============================
collecting ... collected 3 items

test_discount.py::test_ten_per_cent_off_a_round_price PASSED           [ 33%]
test_discount.py::test_nothing_off_leaves_the_price_alone PASSED       [ 66%]
test_discount.py::test_a_silly_percentage_is_refused PASSED            [100%]

============================= 3 passed in 0.00s ==============================
```

## How to check

`./check m02l01-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -v --no-header test_discount.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
