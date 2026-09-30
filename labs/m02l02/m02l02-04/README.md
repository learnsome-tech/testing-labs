# m02l02-04 · Giving each case a name

**Lesson:** [Parametrised Tests](https://learnsome.tech/learn/testing-course/m02l02) (lesson 2.2, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can check one claim against many examples with a parametrised test, give each case a readable identifier, and say when cases should be separate tests instead.

In the lesson: Auto generated identifiers are readable when the data is short numbers, and unreadable the moment your cases are dictionaries or objects, where you get things like case zero and case one. So name them: one identifier per case, in the same order as the data. Read the summary now. Instead of numbers in brackets you get half penny and single penny, which is the vocabulary a human would use in a bug report. Naming cases costs one line and pays for itself the first time somebody who is not you reads the failure.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_discount.py`](starter/test_discount.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `test_discount.py`.
3. Notes from the lesson:
   - Line 9: One identifier per case, in the same order as the data
4. Run it: `python3 -m pytest -q --tb=no test_discount.py`.
5. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
..FF                                                                   [100%]
========================== short test summary info ===========================
FAILED test_discount.py::test_a_tenth_off[half-penny] - assert 895 == 896
 +  where 895 = discounted(995, 10)
FAILED test_discount.py::test_a_tenth_off[single-penny] - assert 0 == 1
 +  where 0 = discounted(1, 10)
2 failed, 2 passed in 0.01s
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=no test_discount.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
