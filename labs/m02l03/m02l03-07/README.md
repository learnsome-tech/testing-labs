# m02l03-07 · Setup and teardown, in order

**Lesson:** [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) (lesson 2.3, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

In the lesson: Now the whole life cycle, twice. Open, one entry added, close reporting one entry. Then open again, and this time the ledger arrives empty, which is the claim the second test makes. Function scope plus teardown is the combination that makes tests independent, and independence is what lets you run them in any order, in parallel, or one at a time while you debug. Everything else in this module is convenience. This is the property that makes a suite trustworthy.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/conftest.py`](starter/conftest.py)
- [`starter/test_ledger.py`](starter/test_ledger.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-07/starter`
2. Read `test_ledger.py`.
3. Run it: `python3 -m pytest -q -s test_ledger.py`.
4. Check it from the repository root: `./check m02l03-07`.

## Expected output

```text
open the ledger
.close the ledger, entries: 1
open the ledger
.close the ledger, entries: 0

2 passed in 0.00s
```

## How to check

`./check m02l03-07` copies `starter/` into a scratch directory and runs `python3 -m pytest -q -s test_ledger.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
