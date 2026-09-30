# m01l03 · One Assertion Per Reason

Module 1: What A Test Is For · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/testing-course/m01l03)

**Goal:** You can split a test so that each one fails for exactly one reason, and you can explain why the first failing assertion hides every assertion after it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | Code with two bugs in it | Read along |
| [m01l03-03](m01l03-03/) | Three claims in one test | Graded |
| [m01l03-04](m01l03-04/) | Three claims in three tests | Graded |
| [m01l03-05](m01l03-05/) | A function that returns several things | Read along |
| [m01l03-06](m01l03-06/) | Three assertions, one reason | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: split a test that hides things

1. Find a test in your suite with assertions about two different behaviours.
2. Break both behaviours at once, run it, and note which failure you were not told about.
3. Split the test, rerun, and check that both failures now appear in the same summary.

> **Hint:** Switch the traceback off while you do this: the summary lines are the point.

## Check yourself

- What is the mechanical reason later assertions do not run after a failure?
- When do several assertions in one test cost you nothing?
- How does a test name tell you it should be split?
- Which flag shows only the summary of failures, with no traceback?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
