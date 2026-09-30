# m03l01 · What Test Doubles Are For

Module 3: Test Doubles And Boundaries · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m03l01)

**Goal:** You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-02](m03l01-02/) | The dependency we cannot call | Read along |
| [m03l01-03](m03l01-03/) | A seam: pass the collaborator in | Read along |
| [m03l01-04](m03l01-04/) | What happens without a double | Graded |
| [m03l01-05](m03l01-05/) | A stub: the smallest thing that answers | Graded |
| [m03l01-06](m03l01-06/) | The error path, on demand | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: find your seams

1. Find one class in your code that constructs its own client, clock or queue.
2. Pass that collaborator in instead, then write the first test for the error path.
3. Note how many tests you can now write that were impossible before.

> **Hint:** If the constructor takes it, the test can supply it: that is the entire technique.

## Check yourself

- Name the four reasons to replace a collaborator in a test.
- What is a seam, and how do you add one?
- Why should you not double a third party library directly?
- Which behaviour is easiest to test with a double and hardest without one?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
