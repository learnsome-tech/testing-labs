# m02l05-06 · Exact equality on a float

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Seven pence at the euro rate is eight point two four six, and the test asserts exactly that. It fails, and the report shows why with brutal clarity: the value carries a tail of nines that no human wrote and no requirement cares about. The arithmetic is correct. The comparison is wrong. If you have ever seen a test that passes on your laptop and fails on a build machine with a different chip or a different library version, this is one of the mechanisms, and it is invisible until the report prints the full value.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/rates.py`](starter/rates.py)
- [`starter/test_rates.py`](starter/test_rates.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-06/starter`
2. Read `test_rates.py`.
3. Run it: `python3 -m pytest -q --tb=short -rN test_rates.py`.
4. Check it from the repository root: `./check m02l05-06`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
_________________________ test_a_conversion_is_exact _________________________
test_rates.py:5: in test_a_conversion_is_exact
    assert convert(7, "EUR") == 8.246
E   AssertionError: assert 8.245999999999999 == 8.246
E    +  where 8.245999999999999 = convert(7, 'EUR')
1 failed in 0.01s
```

## How to check

`./check m02l05-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short -rN test_rates.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
