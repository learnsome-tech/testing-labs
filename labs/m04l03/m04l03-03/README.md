# m04l03-03 · A small contract is executable

**Lesson:** [Contract Testing Between Services](https://learnsome.tech/learn/testing-course/m04l03) (lesson 4.3, module 4: Testing Time, Files And Services) · Pro  
**Check:** Graded

## Goal

You can define a consumer contract, run it against a provider, and see why contract tests connect API design with quality.

In the lesson: Even this small local example is executable contract thinking. The consumer needs an ID and a name, so those are the assertions. A real contract tool would record the request and replay it against the provider, but the quality rule is already visible: assert what the other service promises, and keep implementation detail out of the contract.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_contract.py`](starter/test_contract.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-03/starter`
2. Read `test_contract.py`.
3. Run it: `python3 -m pytest -q test_contract.py`.
4. Check it from the repository root: `./check m04l03-03`.

## Expected output

```text
. [100%]
1 passed in TIMEs
```

## How to check

`./check m04l03-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_contract.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
