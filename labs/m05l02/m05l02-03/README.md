# m05l02-03 · The review checklist is executable too

**Lesson:** [What To Look For In A Review](https://learnsome.tech/learn/testing-course/m05l02) (lesson 5.2, module 5: Quality Gates And Code Review) · Pro  
**Check:** Graded

## Goal

You can review a change for behaviour, boundaries, failure paths and operational risk without getting lost in style debates.

In the lesson: A checklist can be executable in the same modest way as any quality rule. This test says the review questions exist, while the human review asks whether the change answers them. Do not confuse a checklist item with evidence. The value is in making the question easy to remember and the missing answer easy to point at.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_review.py`](starter/test_review.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `test_review.py`.
3. Run it: `python3 -m pytest -q test_review.py`.
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_review.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
