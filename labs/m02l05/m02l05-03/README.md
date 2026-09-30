# m02l05-03 · The anatomy of a failure report

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Here is a wrong expectation on purpose, run with the full traceback, which is what you get by default. Read it from the top. A letter F for the failing test, then a banner, then the test name. Then the body of the test, reprinted, with the marked line carrying a greater than sign: that is where execution stopped. Then the lines starting with E, which are pytest talking rather than your code: the assertion as it was evaluated, with real values in place of expressions. Then the file and line number, and the class of error.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/invoice.py`](starter/invoice.py)
- [`starter/test_invoice.py`](starter/test_invoice.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `test_invoice.py`.
3. Notes from the lesson:
   - Line 9: This is the line the report marks with a greater-than sign
4. Run it: `python3 -m pytest -q test_invoice.py`.
5. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
____________________ test_the_invoice_adds_up_every_line _____________________

    def test_the_invoice_adds_up_every_line():
        lines = [(250, 2), (125, 4)]

        total = invoice_total(lines)

>       assert total == 1100
E       assert 1000 == 1100

test_invoice.py:9: AssertionError
========================== short test summary info ===========================
FAILED test_invoice.py::test_the_invoice_adds_up_every_line - assert 1000 == 1100
1 failed in 0.01s
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_invoice.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
