# m01l05-06 · The bug the full report missed

**Lesson:** [Coverage: Diagnostic, Not Target](https://learnsome.tech/learn/testing-course/m01l05) (lesson 1.5, module 1: What A Test Is For) · Pro  
**Check:** Graded

## Goal

You can read a coverage report to find untested branches, and you can demonstrate a suite with full coverage that fails to notice a live bug.

In the lesson: And here is one real assertion about the fee path that the fully covered suite had already run. A full return of a thousand pence with a fifty penny restocking fee should hand back nine hundred and fifty. The code hands back minus fifty, because the fee is taken off the difference rather than off the amount returned. The line was covered. The behaviour was never checked. Coverage saw the code run and had no opinion about the answer, which is exactly what it promised to do, and exactly why it is a diagnostic and never a target.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/refund.py`](starter/refund.py)
- [`starter/test_refund.py`](starter/test_refund.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-06/starter`
2. Read `test_refund.py`.
3. Run it: `python3 -m pytest -q --tb=short test_refund.py`.
4. Check it from the repository root: `./check m01l05-06`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
_________________ test_a_restocking_fee_comes_off_the_refund _________________
test_refund.py:5: in test_a_restocking_fee_comes_off_the_refund
    assert refund(1000, 1000, restocking_fee=50) == 950
E   assert -50 == 950
E    +  where -50 = refund(1000, 1000, restocking_fee=50)
========================== short test summary info ===========================
FAILED test_refund.py::test_a_restocking_fee_comes_off_the_refund - assert -50 == 950
 +  where -50 = refund(1000, 1000, restocking_fee=50)
1 failed in 0.01s
```

## How to check

`./check m01l05-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short test_refund.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
