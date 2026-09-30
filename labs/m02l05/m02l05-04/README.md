# m02l05-04 · How pytest compares collections

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Now compare two lists and watch what the assertion rewriting does for you. It does not merely tell you the two lists differ. It says which side has the extra item and names it, then prints a diff with the missing entry marked. The same treatment applies to dictionaries, sets and long strings, where it names the differing keys and omits the identical ones. This is why the plain assert statement is enough in Python, and why reaching for a special assertion function usually costs you information rather than adding it.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/invoice.py`](starter/invoice.py)
- [`starter/test_invoice.py`](starter/test_invoice.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-04/starter`
2. Read `test_invoice.py`.
3. Run it: `python3 -m pytest -q --tb=short -rN test_invoice.py`.
4. Check it from the repository root: `./check m02l05-04`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
______________________ test_the_names_are_kept_in_order ______________________
test_invoice.py:7: in test_the_names_are_kept_in_order
    assert line_names(lines) == ["tea", "jam", "cake"]
E   AssertionError: assert ['tea', 'jam'] == ['tea', 'jam', 'cake']
E
E     Right contains one more item: 'cake'
E
E     Full diff:
E       [
E           'tea',
E           'jam',
E     -     'cake',
E       ]
1 failed in 0.01s
```

## How to check

`./check m02l05-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short -rN test_invoice.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
