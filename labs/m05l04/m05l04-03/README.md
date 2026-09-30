# m05l04-03 · A comment can be checked

**Lesson:** [Writing Actionable Review Comments](https://learnsome.tech/learn/testing-course/m05l04) (lesson 5.4, module 5: Quality Gates And Code Review) · Pro  
**Check:** Graded

## Goal

You can write review comments that name the risk, point to evidence, and give the author a clear next action.

In the lesson: Even a review template can be checked for the parts that make it useful. This example contains the risk and a next action. In real work, the reviewer still supplies context and evidence; a template only keeps the shape visible. Before submitting, read the comment as the author will read it after a long day. Can they locate the concern and make a concrete change?

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_comment.py`](starter/test_comment.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `test_comment.py`.
3. Run it: `python3 -m pytest -q test_comment.py`.
4. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_comment.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
