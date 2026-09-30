# m01l04 · The Test Pyramid And Where It Is Wrong

Module 1: What A Test Is For · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/testing-course/m01l04)

**Goal:** You can explain what the test pyramid is really a picture of, mark the slow tests in your suite, and select or deselect them by marker.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-03](m01l04-03/) | Registering a marker | Read along |
| [m01l04-04](m01l04-04/) | The module both layers touch | Read along |
| [m01l04-05](m01l04-05/) | What the layers cost, in seconds | Graded |
| [m01l04-06](m01l04-06/) | Choosing a layer by marker | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: measure your own shape

1. Run your suite with the durations flag and write down the ten slowest tests.
2. For each, note what it needs alive: a database, a browser, a network, a clock.
3. Mark those tests, then run the suite without them and compare the two times.

> **Hint:** If the fast selection is not fast enough to run on every save, keep going up the list.

## Check yourself

- What two things increase as you move up the pyramid?
- Why is a unit test of a thin database layer often worthless?
- Which command runs everything except the tests you marked slow?
- Name two alternative shapes and what each one weights.
- What does the durations flag tell you that a total runtime does not?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
