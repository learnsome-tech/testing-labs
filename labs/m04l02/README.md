# m04l02 · Integration Testing With Containers

Module 4: Testing Time, Files And Services · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m04l02)

**Goal:** You can decide when an integration test needs a real dependency, start it with a disposable container, and keep the test boundary explicit.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-04](m04l02-04/) | A disposable database fixture | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: one real boundary

1. Pick one dependency whose wire contract matters.
2. Write a disposable container fixture with a health check.
3. Run one happy path and one migration or timeout failure.

> **Hint:** Pin the image and make readiness a condition, not a sleep.

## Check yourself

- What does an integration test add beyond a unit test?
- Why is a health check stronger than a sleep?
- Who owns container cleanup?
- When should a container demo be marked noVerify?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
