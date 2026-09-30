# m05l01-03 · The gate runs a real check

**Lesson:** [Code Review As A Quality Gate](https://learnsome.tech/learn/testing-course/m05l01) (lesson 5.1, module 5: Quality Gates And Code Review) · Pro  
**Check:** Graded

## Goal

You can treat review as a quality gate, combine human judgement with automated checks, and ask whether a change is safe to merge.

In the lesson: This tiny test stands for the automated layer of the gate. It runs a real assertion and reports a real pass. In a project the command would include lint, types, unit tests and the focused integration suite. Keep the commands reproducible and make failures visible in the pull request, so the reviewer can spend attention on the change rather than asking whether the checks ran.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_gate.py`](starter/test_gate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `test_gate.py`.
3. Run it: `python3 -m pytest -q test_gate.py`.
4. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_gate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
