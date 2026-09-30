# m03l03-04 · The real contract exposes it

**Lesson:** [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) (lesson 3.3, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

In the lesson: Now run the same claim against a small working implementation of the gateway contract. This is not a network call. It is a fake with the real response shape, and the test fails for the useful reason: key error ID. Read that failure as a design review. The test did not need to know how many calls happened. It needed to know what a customer receives after a successful charge. A fake has found the mismatch that the mock concealed, and it has done so in milliseconds.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_contract_shape.py`](starter/test_contract_shape.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `test_contract_shape.py`.
3. Run it: `python3 -m pytest -q --tb=no test_contract_shape.py`.
4. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
F [100%]
=== short test summary info ===
FAILED test_contract_shape.py::test_pay_uses_the_gateway_contract - KeyErro...
1 failed in TIMEs
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=no test_contract_shape.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
