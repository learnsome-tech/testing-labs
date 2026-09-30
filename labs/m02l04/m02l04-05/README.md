# m02l04-05 · The same tests, renamed

**Lesson:** [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) (lesson 2.4, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can name tests so that a failure summary reads as a sentence, and use those names to select subsets of the suite from the command line.

In the lesson: Same three tests, same three assertions, renamed. Collect them again and the list is now a specification: a tenth off a thousand pence leaves nine hundred, no discount leaves the price untouched, a full discount makes the price zero. Anybody can audit that list against what the business actually wants, including people who do not read Python. Long names are fine here. Nobody types them, the editor completes them, and the cost of a long name is paid once while the benefit arrives on every failure.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_names.py`](starter/test_names.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-05/starter`
2. Read `test_names.py`.
3. Run it: `python3 -m pytest -q --collect-only test_names.py`.
4. Check it from the repository root: `./check m02l04-05`.

## Expected output

```text
test_names.py::test_a_tenth_off_a_thousand_pence_leaves_nine_hundred
test_names.py::test_no_discount_leaves_the_price_untouched
test_names.py::test_a_full_discount_makes_the_price_zero

3 tests collected in 0.00s
```

## How to check

`./check m02l04-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --collect-only test_names.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
