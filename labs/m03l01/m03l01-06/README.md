# m03l01-06 · The error path, on demand

**Lesson:** [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) (lesson 3.1, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

In the lesson: And now the interesting half, the reason doubles are worth the trouble at all. This double raises the timeout instead of answering. The test asserts that a timeout leaves the customer with nothing rather than a half confirmed order. You cannot get the real gateway to time out when you ask it to; you can only wait for a bad afternoon. With a double, the bad afternoon is a test that runs on every commit, and the error path stops being the code nobody has ever executed.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/gateway.py`](starter/gateway.py)
- [`starter/test_timeout.py`](starter/test_timeout.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-06/starter`
2. Read `test_timeout.py`.
3. Run it: `python3 -m pytest -q test_timeout.py`.
4. Check it from the repository root: `./check m03l01-06`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l01-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_timeout.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
