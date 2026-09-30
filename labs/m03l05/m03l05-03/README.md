# m03l05-03 · A temporary path leaves no residue

**Lesson:** [Testing The Filesystem](https://learnsome.tech/learn/testing-course/m03l05) (lesson 3.5, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can test filesystem behaviour with pytest temporary paths, assert the visible file contract, and avoid leaking state between tests.

In the lesson: The test receives a fresh temporary path from pytest. It calls the writer, then checks three observable facts: the file name, the exact text read back with the declared encoding, and the parent directory. The directory is unique to this test, so no other test can make these assertions pass accidentally. When pytest finishes, the temporary path is removed. In other ecosystems the names differ, but the idea is the same: JUnit has temporary directory extensions, and JavaScript runners often provide a temporary directory helper.

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

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `test_report.py`.
3. Run it: `python3 -m pytest -q test_report.py`.
4. Check it from the repository root: `./check m03l05-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_report.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
