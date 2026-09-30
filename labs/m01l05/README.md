# m01l05 · Coverage: Diagnostic, Not Target

Module 1: What A Test Is For · lesson 1.5 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m01l05)

**Goal:** You can read a coverage report to find untested branches, and you can demonstrate a suite with full coverage that fails to notice a live bug.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-02](m01l05-02/) | A function with branches | Read along |
| [m01l05-03](m01l05-03/) | Covering the happy path only | Graded |
| [m01l05-05](m01l05-05/) | Full coverage that checks nothing | Graded |
| [m01l05-06](m01l05-06/) | The bug the full report missed | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: read your own missing column

1. Run your suite with coverage and the missing report, then sort the gaps by risk.
2. Pick the riskiest uncovered line and write the test that would have caught a bug there.
3. Find one test in your suite that runs code without asserting anything about it.

> **Hint:** Error handling and money are where uncovered lines hurt most.

## Check yourself

- What is the difference between line coverage and branch coverage?
- Which part of the coverage report should you read first, and why?
- How can a suite reach full coverage while missing an obvious bug?
- Why does a coverage percentage make a poor build gate?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
