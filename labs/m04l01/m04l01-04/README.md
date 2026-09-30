# m04l01-04 · The fixed instant stays green

**Lesson:** [Flaky Tests And How To Kill Them](https://learnsome.tech/learn/testing-course/m04l01) (lesson 4.1, module 4: Testing Time, Files And Services) · Pro  
**Check:** Graded

## Goal

You can identify a flaky test, reproduce the moving input, and replace timing luck with a deterministic boundary.

In the lesson: The repaired test supplies one fixed instant and passes every time. It does not sleep, retry or depend on the machine clock. A useful debugging loop for a flaky test is to run it repeatedly, randomise test order, and run it alone and in the full suite. Once the cause is known, delete the luck and keep the smallest deterministic test that states the intended behaviour.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/clocked.py`](starter/clocked.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_clocked.py`](starter/test_clocked.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `test_clocked.py`.
3. Run it: `python3 -m pytest -q test_clocked.py`.
4. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_clocked.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
