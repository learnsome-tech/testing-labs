# m03l03 · Why Over-Mocking Breeds False Positives

Module 3: Test Doubles And Boundaries · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m03l03)

**Goal:** You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | A bug hidden by a mock | Read along |
| [m03l03-03](m03l03-03/) | The mock makes the bug look green | Graded |
| [m03l03-04](m03l03-04/) | The real contract exposes it | Graded |
| [m03l03-05](m03l03-05/) | Fix the behaviour, then simplify | Read along |
| [m03l03-06](m03l03-06/) | A behavioural test stays useful | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: find a false positive

1. Search for a mock whose return value is invented in the test.
2. Run the claim against a small fake with the real response shape.
3. Rewrite the assertion around an observable result or a real message.

> **Hint:** If the test would still pass after deleting the collaborator implementation, it is testing the script, not the system.

## Check yourself

- What makes a passing mock test a false positive?
- When is an interaction assertion the behaviour you need to check?
- Why did the small fake find a bug the mock concealed?
- What should a durable test observe?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
