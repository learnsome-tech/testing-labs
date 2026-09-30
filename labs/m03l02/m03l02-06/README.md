# m03l02-06 · A fake, which really works

**Lesson:** [Fakes, Stubs, Mocks And Spies](https://learnsome.tech/learn/testing-course/m03l02) (lesson 3.2, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can name and write the four kinds of test double, and choose between them by what the test needs to observe.

In the lesson: And a fake, which is the most valuable and the least fashionable of the four. It really implements the interface, in memory, including a rule the real gateway has: the same reference cannot be charged twice. The fake passes, and it can be reused by every test in the suite, including tests that need two calls to interact. Fakes cost more to write and they can drift from the real thing, which is what contract testing is for later in this course. What you get in return is tests that exercise behaviour instead of rehearsing call sequences.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_fake.py`](starter/test_fake.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-06/starter`
2. Read `test_fake.py`.
3. Run it: `python3 -m pytest -q test_fake.py`.
4. Check it from the repository root: `./check m03l02-06`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l02-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_fake.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
