# m03l04-03 · Freeze time at both sides of the boundary

**Lesson:** [Testing Time And Randomness](https://learnsome.tech/learn/testing-course/m03l04) (lesson 3.4, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can make time and randomness explicit dependencies, freeze them in pytest, and test boundary behaviour without sleeps or lucky seeds.

In the lesson: The two tests freeze the clock at one instant and check both sides of the boundary. There is no sleep, no dependence on the date on this machine, and no flaky race between the assertion and the clock tick. The first test says one second after now is active, and the second says exactly now is not. If your policy is inclusive instead, write that word into the test and change the comparison deliberately. A fixed input makes the failure explain the rule rather than the machine.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/session.py`](starter/session.py)
- [`starter/test_session.py`](starter/test_session.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-03/starter`
2. Read `test_session.py`.
3. Run it: `python3 -m pytest -q test_session.py`.
4. Check it from the repository root: `./check m03l04-03`.

## Expected output

```text
.. [100%]
2 passed in TIMEs
```

## How to check

`./check m03l04-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_session.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
