# m03l04-05 · Choose the result on purpose

**Lesson:** [Testing Time And Randomness](https://learnsome.tech/learn/testing-course/m03l04) (lesson 3.4, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can make time and randomness explicit dependencies, freeze them in pytest, and test boundary behaviour without sleeps or lucky seeds.

In the lesson: The test supplies a generator with one deliberate answer and checks the result. The double is not pretending to be random. It is removing randomness so the claim can be deterministic. Keep a separate test for the generator adapter if you need confidence that the standard library is wired correctly. In the function under test, focus on what your service promises after it receives a choice. Other ecosystems use injected random sources too: Java has a random generator interface, and JavaScript often passes a function.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/invite.py`](starter/invite.py)
- [`starter/test_invite.py`](starter/test_invite.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-05/starter`
2. Read `test_invite.py`.
3. Run it: `python3 -m pytest -q test_invite.py`.
4. Check it from the repository root: `./check m03l04-05`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l04-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_invite.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
