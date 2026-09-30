# m03l02-05 · A mock, which complains for itself

**Lesson:** [Fakes, Stubs, Mocks And Spies](https://learnsome.tech/learn/testing-course/m03l02) (lesson 3.2, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can name and write the four kinds of test double, and choose between them by what the test needs to observe.

In the lesson: A mock from the standard library. Two things to notice. The double is built with autospec, which copies the real signature, so a wrong call is refused instead of silently accepted: that is the difference between a mock that helps you and a mock that lies, and the next lesson is about exactly that. And the assertion is made by the double, not by you: it was told what call to expect and it raises when the call differs. This passes too. The test now depends on the argument order of somebody else's method, which is a real cost.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/gateway.py`](starter/gateway.py)
- [`starter/test_mock.py`](starter/test_mock.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-05/starter`
2. Read `test_mock.py`.
3. Notes from the lesson:
   - Line 8: autospec copies the real signature, so a wrong call is refused
4. Run it: `python3 -m pytest -q test_mock.py`.
5. Check it from the repository root: `./check m03l02-05`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l02-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_mock.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
