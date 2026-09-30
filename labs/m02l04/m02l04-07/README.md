# m02l04-07 · Names as a query language

**Lesson:** [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) (lesson 2.4, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can name tests so that a failure summary reads as a sentence, and use those names to select subsets of the suite from the command line.

In the lesson: And here is the practical payoff beyond reading. Because the names carry domain words, you can select on a phrase: everything about full discounts, everything about refunds, everything mentioning currency. One passed, two deselected. With numbered names the only possible selection is by file. Good names turn your suite into something you can slice while you work, which matters most in the exact situation where the suite is big and slow and you are trying to move quickly.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_names.py`](starter/test_names.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-07/starter`
2. Read `test_names.py`.
3. Run it: `python3 -m pytest -q -k full_discount test_names.py`.
4. Check it from the repository root: `./check m02l04-07`.

## Expected output

```text
.                                                                      [100%]
1 passed, 2 deselected in 0.00s
```

## How to check

`./check m02l04-07` copies `starter/` into a scratch directory and runs `python3 -m pytest -q -k full_discount test_names.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
