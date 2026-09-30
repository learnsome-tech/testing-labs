# m03l03-06 · A behavioural test stays useful

**Lesson:** [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) (lesson 3.3, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

In the lesson: Run the repaired test. It passes against the working contract, and it would keep passing if the gateway gained an internal retry or changed its client library. That is a durable test: it observes the returned reference, which is the promise your function makes. Keep interaction assertions for behaviour that really is a message, such as sending one email or publishing one event. For ordinary calculations and translations, prefer the answer over the choreography.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_contract_shape.py`](starter/test_contract_shape.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-06/starter`
2. Read `test_contract_shape.py`.
3. Run it: `python3 -m pytest -q test_contract_shape.py`.
4. Check it from the repository root: `./check m03l03-06`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m03l03-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_contract_shape.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
