# m03l01-04 · What happens without a double

**Lesson:** [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) (lesson 3.1, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Graded

## Goal

You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

In the lesson: Before the double, the motivation. Run it against the real client and the test does not fail in an interesting way: it fails because the collaborator refuses to be used like this. In your own codebase you would see a connection error, or worse, a real payment and a test that passes on a Tuesday and empties a budget by Friday. The report also shows something useful for later: the traceback walks from the test into the code under test and then into the collaborator, which is exactly the boundary we are about to cut.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/checkout.py`](starter/checkout.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/gateway.py`](starter/gateway.py)
- [`starter/test_real.py`](starter/test_real.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `test_real.py`.
3. Run it: `python3 -m pytest -q --tb=short -rN test_real.py`.
4. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
F [100%]
=== FAILURES ===
___ test_paying_with_the_real_gateway ___
test_real.py:6: in test_paying_with_the_real_gateway
    assert pay(Gateway(), 1000, "abc") == "abc"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
checkout.py:7: in pay
    receipt = gateway.charge(pence, reference)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gateway.py:9: in charge
    raise RuntimeError("this would reach the network")
E   RuntimeError: this would reach the network
1 failed in TIMEs
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short -rN test_real.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
