# m04l05 · Testing With Real Databases

Module 4: Testing Time, Files And Services · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m04l05)

**Goal:** You can choose database tests that deserve a real engine, isolate their data, and verify migrations and transactions without shared state.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | A local storage contract | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: test one engine promise

1. Choose one migration, constraint or transaction rule.
2. Run it against the real database engine.
3. Make the fixture clean its schema after the test.

> **Hint:** Test the engine behaviour your fake cannot know, not every business rule twice.

## Check yourself

- What can a fake database miss?
- How can database tests isolate their state?
- Why should row order be explicit?
- Which claims belong in unit tests instead?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
