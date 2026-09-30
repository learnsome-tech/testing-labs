# m04l01 · Flaky Tests And How To Kill Them

Module 4: Testing Time, Files And Services · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m04l01)

**Goal:** You can identify a flaky test, reproduce the moving input, and replace timing luck with a deterministic boundary.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-02](m04l01-02/) | The time dependent test fails for real | Read along |
| [m04l01-03](m04l01-03/) | Move the clock behind a seam | Read along |
| [m04l01-04](m04l01-04/) | The fixed instant stays green | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: kill one flake

1. Run one flaky test repeatedly and record the moving input.
2. Replace that input with a seam or an isolated fixture.
3. Remove any retry added only to hide the failure.

> **Hint:** A retry is a clue that the test still depends on something outside its control.

## Check yourself

- What makes a test flaky?
- Why is retrying a weak fix?
- Which input moves in the failing example?
- How does a seam make the verdict stable?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
