# m02l02-06 · Every case, by name

**Lesson:** [Parametrised Tests](https://learnsome.tech/learn/testing-course/m02l02) (lesson 2.2, module 2: Unit Testing In Practice) · Pro  
**Check:** Graded

## Goal

You can check one claim against many examples with a parametrised test, give each case a readable identifier, and say when cases should be separate tests instead.

In the lesson: Run them verbosely, and there is the point of the whole lesson on one screen: four addresses, four verdicts, one test body. Any one of those identifiers can be pasted back onto the command line, in quotes because of the brackets, to rerun a single case while you debug it. When a case fails in continuous integration six weeks from now, the log will name it in the language of the domain. And when somebody finds a new awkward price, the fix is one line of data, not another copied test.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/discount.py`](starter/discount.py)
- [`starter/test_discount.py`](starter/test_discount.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-06/starter`
2. Read `test_discount.py`.
3. Run it: `python3 -m pytest -v --no-header test_discount.py`.
4. Check it from the repository root: `./check m02l02-06`.

## Expected output

```text
============================ test session starts =============================
collecting ... collected 4 items

test_discount.py::test_a_tenth_off[round] PASSED                       [ 25%]
test_discount.py::test_a_tenth_off[off-by-a-penny] PASSED              [ 50%]
test_discount.py::test_a_tenth_off[half-penny] PASSED                  [ 75%]
test_discount.py::test_a_tenth_off[single-penny] PASSED                [100%]

============================= 4 passed in 0.00s ==============================
```

## How to check

`./check m02l02-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -v --no-header test_discount.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
