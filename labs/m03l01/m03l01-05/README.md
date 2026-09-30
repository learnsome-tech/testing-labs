# m03l01-05 · A stub: the smallest thing that answers

**Lesson:** [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) (lesson 3.1, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

In the lesson: Here is the double, hand written, eight lines including the docstring. It has the same method with the same parameters, it answers the way the real gateway answers on a good day, and it records nothing. The test passes, in about a millisecond, with no network and no secret key. This is a stub: a canned answer. Most of the time, in most codebases, this is the only kind of double you need, and writing it by hand keeps you honest about what the real collaborator actually returns.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/gateway.py`](starter/gateway.py)
- [`starter/test_checkout.py`](starter/test_checkout.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-05/starter`
2. Read `test_checkout.py`.
3. Run it: `python3 -m pytest -q test_checkout.py`.
4. Check it from the repository root: `./check m03l01-05`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l01-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_checkout.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
