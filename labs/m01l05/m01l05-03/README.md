# m01l05-03 · Covering the happy path only

**Lesson:** [Coverage: Diagnostic, Not Target](https://learnsome.tech/learn/testing-course/m01l05) (lesson 1.5, module 1: What A Test Is For) · Pro  
**Check:** Graded

## Goal

You can read a coverage report to find untested branches, and you can demonstrate a suite with full coverage that fails to notice a live bug.

In the lesson: Two honest tests of the ordinary path, run with coverage measurement switched on. Both pass, and the report earns its keep in the missing column: it names the lines that never ran. Those are the raise and the fee. This is coverage being genuinely useful, and it is the way to use it: not as a score, but as a list of code your suite has never once executed. Every line in that column is a question. Sometimes the answer is that the line cannot happen and should be deleted. Usually the answer is that nobody got round to it.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/refund.py`](starter/refund.py)
- [`starter/test_refund.py`](starter/test_refund.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-03/starter`
2. Read `test_refund.py`.
3. Run it: `python3 -m pytest -q --cov=refund --cov-report=term-missing test_refund.py`.
4. Check it from the repository root: `./check m01l05-03`.

## Expected output

```text
..                                                                     [100%]
=============================== tests coverage ===============================
______________ coverage: platform darwin, python 3.14.7-final-0 ______________

Name        Stmts   Miss  Cover   Missing
-----------------------------------------
refund.py       6      2    67%   4, 6
-----------------------------------------
TOTAL           6      2    67%
2 passed in 0.01s
```

## How to check

`./check m01l05-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --cov=refund --cov-report=term-missing test_refund.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
