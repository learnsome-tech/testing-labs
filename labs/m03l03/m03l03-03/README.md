# m03l03-03 · The mock makes the bug look green

**Lesson:** [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) (lesson 3.3, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

In the lesson: Run the mock test. It passes, because the mock was configured with the same wrong field the implementation reads. The test has checked that one invented conversation happened, and nothing about the real gateway contract. This is a false positive: a passing test that would let a broken production behaviour through. Notice the seductive shape. The test is fast, isolated and tidy. Those are useful properties, but they are not the same thing as truth. Isolation is a means, not the assertion.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_mocked_checkout.py`](starter/test_mocked_checkout.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `test_mocked_checkout.py`.
3. Run it: `python3 -m pytest -q test_mocked_checkout.py`.
4. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_mocked_checkout.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
