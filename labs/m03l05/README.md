# m03l05 · Testing The Filesystem

Module 3: Test Doubles And Boundaries · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m03l05)

**Goal:** You can test filesystem behaviour with pytest temporary paths, assert the visible file contract, and avoid leaking state between tests.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | Write a report to a supplied directory | Read along |
| [m03l05-03](m03l05-03/) | A temporary path leaves no residue | Graded |
| [m03l05-04](m03l05-04/) | Missing input is a deliberate case | Read along |
| [m03l05-05](m03l05-05/) | Check both present and absent | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: isolate a file contract

1. Find a function that writes to a fixed path and give it a destination seam.
2. Use tmp_path to test its file name and exact contents.
3. Add a missing file or cleanup case and run the test twice.

> **Hint:** Keep each test's temporary path private; do not clean a shared folder by hand.

## Check yourself

- Why is a hard coded test path unsafe?
- What three facts does the writer test assert?
- How does a temporary path prevent accidental test coupling?
- Who should own cleanup for a resource created in a test?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
