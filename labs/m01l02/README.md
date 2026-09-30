# m01l02 · Arrange, Act, Assert

Module 1: What A Test Is For · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/testing-course/m01l02)

**Goal:** You can write a test in three visible phases, and you can show that the phases make the failure report easier to read than a one line test.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | The module we will be pricing with | Read along |
| [m01l02-03](m01l02-03/) | The three phases, separated by blank lines | Graded |
| [m01l02-04](m01l02-04/) | Somebody changes the rate | Read along |
| [m01l02-05](m01l02-05/) | How a phased test fails | Graded |
| [m01l02-06](m01l02-06/) | The same test, all on one line | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: find the act

1. Take three tests from a suite you work on and mark the arrange, act and assert in each.
2. Any test with no single act line is doing two jobs: split it and rerun both halves.
3. Rewrite one nested assertion so the result has a name, then break the code and compare.

> **Hint:** The act is the call whose result the assertion talks about, and there should be one.

## Check yourself

- What are the three phases of a test, in order?
- Why does the act deserve a line and a name of its own?
- What goes wrong when a test computes its expectation from the code under test?
- Why does a one line test produce a longer failure report?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
