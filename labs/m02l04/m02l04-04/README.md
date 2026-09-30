# m02l04-04 · What collection shows you

**Lesson:** [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) (lesson 2.4, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can name tests so that a failure summary reads as a sentence, and use those names to select subsets of the suite from the command line.

In the lesson: You do not need a failure to judge names. Ask pytest to collect without running anything, and it prints the identifier of every test it found. Read that list as though you were an on call engineer at three in the morning, which is the real audience. It tells you that there are three tests about discounts, and nothing else whatsoever. This command is also the fastest way to see that a test you expected is missing, and it costs nothing because no test body is executed.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_names.py`](starter/test_names.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `test_names.py`.
3. Run it: `python3 -m pytest -q --collect-only test_names.py`.
4. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
test_names.py::test_discount1
test_names.py::test_discount2
test_names.py::test_discount_edge

3 tests collected in 0.00s
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --collect-only test_names.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
