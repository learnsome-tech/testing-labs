# m05l03-03 · A required check really runs

**Lesson:** [What To Automate Away](https://learnsome.tech/learn/testing-course/m05l03) (lesson 5.3, module 5: Quality Gates And Code Review) · Pro  
**Check:** Graded

## Goal

You can automate mechanical review work, keep policy visible in tools, and reserve human attention for decisions automation cannot make.

In the lesson: This example keeps the policy visible as data: the required checks have names and an order. Your real pipeline can express the same policy in a workflow file, with separate jobs and clear failure messages. The point is not the list itself. It is that the gate should be inspectable, runnable and boring enough that nobody has to remember a private ritual.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_automation.py`](starter/test_automation.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `test_automation.py`.
3. Run it: `python3 -m pytest -q test_automation.py`.
4. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_automation.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
