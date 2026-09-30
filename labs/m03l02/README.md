# m03l02 · Fakes, Stubs, Mocks And Spies

Module 3: Test Doubles And Boundaries · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m03l02)

**Goal:** You can name and write the four kinds of test double, and choose between them by what the test needs to observe.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | The interface all four stand in for | Read along |
| [m03l02-03](m03l02-03/) | The small seam used by each double | Read along |
| [m03l02-04](m03l02-04/) | A stub and a spy | Graded |
| [m03l02-05](m03l02-05/) | A mock, which complains for itself | Graded |
| [m03l02-06](m03l02-06/) | A fake, which really works | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: name the doubles you have

1. Open your suite and classify five doubles as stub, spy, mock, fake or dummy.
2. Find one mock that only ever provides an answer, and simplify it to a stub.
3. Find one collaborator used by many tests, and write one shared fake for it.

> **Hint:** If nothing ever asserts on the recorded calls, the double is a stub in disguise.

## Check yourself

- What is the difference between a stub and a spy?
- What does a mock do that the other doubles do not?
- When is a fake worth the extra code it costs?
- What is a dummy, and when would you pass one?
- Why does a mock couple your test to argument order?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
