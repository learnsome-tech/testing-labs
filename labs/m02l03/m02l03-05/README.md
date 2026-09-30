# m02l03-05 · A wide scope that leaks

**Lesson:** [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) (lesson 2.3, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

In the lesson: Here are two tests using that module scoped price list, and the first one adds an item to it. The second test fails, and read carefully what it says: three is not two, and the dictionary in the report has a cake in it that this test never put there. The first test passed. Neither test is wrong on its own. Run the second one by itself and it passes. This is a shared mutable fixture, it is a real bug in a real suite, and the failure will move around as soon as somebody reorders the file.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/conftest.py`](starter/conftest.py)
- [`starter/test_leak.py`](starter/test_leak.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-05/starter`
2. Read `test_leak.py`.
3. Run it: `python3 -m pytest -q --tb=short test_leak.py`.
4. Check it from the repository root: `./check m02l03-05`.

## Expected output

```text
.F                                                                     [100%]
================================== FAILURES ==================================
______________________ test_the_price_list_is_untouched ______________________
test_leak.py:7: in test_the_price_list_is_untouched
    assert len(price_list) == 2
E   AssertionError: assert 3 == 2
E    +  where 3 = len({'tea': 250, 'jam': 125, 'cake': 400})
========================== short test summary info ===========================
FAILED test_leak.py::test_the_price_list_is_untouched - AssertionError: assert 3 == 2
 +  where 3 = len({'tea': 250, 'jam': 125, 'cake': 400})
1 failed, 1 passed in 0.01s
```

## How to check

`./check m02l03-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short test_leak.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
