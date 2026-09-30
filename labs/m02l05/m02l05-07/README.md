# m02l05-07 · Approximate comparison, and a message

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Two fixes on one screen. The approx helper compares with a tolerance, by default a relative one, and you can pass an absolute tolerance when you know how many pence matter. The raises block takes a match argument, which is a regular expression checked against the text of the error, so the test pins not only that something was refused but that the message names the currency. Both pass. Without the match argument, that second test would also pass if the code raised a key error for an entirely different reason, which is a false pass waiting to happen.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/rates.py`](starter/rates.py)
- [`starter/test_rates.py`](starter/test_rates.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-07/starter`
2. Read `test_rates.py`.
3. Notes from the lesson:
   - Line 11: match is a regular expression checked against the error text
4. Run it: `python3 -m pytest -q test_rates.py`.
5. Check it from the repository root: `./check m02l05-07`.

## Expected output

```text
..                                                                     [100%]
2 passed in 0.00s
```

## How to check

`./check m02l05-07` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_rates.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
