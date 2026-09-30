# m03l05-05 · Check both present and absent

**Lesson:** [Testing The Filesystem](https://learnsome.tech/learn/testing-course/m03l05) (lesson 3.5, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can test filesystem behaviour with pytest temporary paths, assert the visible file contract, and avoid leaking state between tests.

In the lesson: These two tests cover the two file states without sharing state. The first starts with an empty temporary directory and checks the missing policy. The second creates one file through the public writer and reads it through the public reader. That pairing catches mismatched encodings, names and paths while keeping setup close to the reason for each test. If a test needs a large tree of files, build it with a fixture, but keep the fixture scope as narrow as the state allows.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/report.py`](starter/report.py)
- [`starter/test_report.py`](starter/test_report.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-05/starter`
2. Read `test_report.py`.
3. Run it: `python3 -m pytest -q test_report.py`.
4. Check it from the repository root: `./check m03l05-05`.

## Expected output

```text
.. [100%]
2 passed in TIMEs
```

## How to check

`./check m03l05-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_report.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
