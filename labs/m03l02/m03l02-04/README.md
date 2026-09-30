# m03l02-04 · A stub and a spy

**Lesson:** [Fakes, Stubs, Mocks And Spies](https://learnsome.tech/learn/testing-course/m03l02) (lesson 3.2, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can name and write the four kinds of test double, and choose between them by what the test needs to observe.

In the lesson: The stub and the spy, side by side, and the difference is one list. The stub supports a claim about the answer: paying gives back the reference. The spy supports a claim about the request: the gateway was asked for a thousand pence, once, with that reference. Both pass. Use a spy when the message sent is the behaviour you care about, which is common at the edge of a system where the whole point of the code is that something was sent. Use a stub everywhere else, because a spy that nobody inspects is a stub with extra lines.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_doubles.py`](starter/test_doubles.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-04/starter`
2. Read `test_doubles.py`.
3. Run it: `python3 -m pytest -q test_doubles.py`.
4. Check it from the repository root: `./check m03l02-04`.

## Expected output

```text
.. [100%]
2 passed in TIMEs
```

## How to check

`./check m03l02-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_doubles.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
