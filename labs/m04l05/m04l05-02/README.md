# m04l05-02 · A local storage contract

**Lesson:** [Testing With Real Databases](https://learnsome.tech/learn/testing-course/m04l05) (lesson 4.5, module 4: Testing Time, Files And Services) · Pro  
**Check:** Graded

## Goal

You can choose database tests that deserve a real engine, isolate their data, and verify migrations and transactions without shared state.

In the lesson: This local test shows the shape of a storage claim, but the set is only a teaching stand in. A real database test would create a temporary schema, apply migrations, insert the first row, then assert the unique constraint rejects the second. The point is to keep the claim narrow and make the real engine responsible for the behaviour a fake cannot model.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_storage.py`](starter/test_storage.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `test_storage.py`.
3. Run it: `python3 -m pytest -q test_storage.py`.
4. Check it from the repository root: `./check m04l05-02`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_storage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
