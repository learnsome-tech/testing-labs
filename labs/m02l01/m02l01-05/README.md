# m02l01-05 · Selecting tests by keyword

**Lesson:** [Introducing pytest](https://learnsome.tech/learn/testing-course/m02l01) (lesson 2.1, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write and run a pytest suite with no configuration, read the session header, and select tests by name from the command line.

In the lesson: You can also select by keyword. The dash k flag takes a substring, or a small expression using and, or and not, and matches it against the test identifiers. One passed, two deselected. Deselected is not skipped and not passed: those tests were never considered part of this run, and the count says so honestly. This is the second reason test names matter, and we will spend a whole lesson on them: the names are the query language you use to drive your own suite.

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

1. Go to the starter: `cd labs/m02l01/m02l01-05/starter`
2. Read `test_discount.py`.
3. Run it: `python3 -m pytest -q -k silly test_discount.py`.
4. Check it from the repository root: `./check m02l01-05`.

## Expected output

```text
.                                                                      [100%]
1 passed, 2 deselected in 0.00s
```

## How to check

`./check m02l01-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q -k silly test_discount.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
