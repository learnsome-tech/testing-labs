# m02l01 · Introducing pytest

Module 2: Unit Testing In Practice · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m02l01)

**Goal:** You can write and run a pytest suite with no configuration, read the session header, and select tests by name from the command line.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | The module under test | Read along |
| [m02l01-03](m02l01-03/) | Running the suite | Graded |
| [m02l01-04](m02l01-04/) | Seeing every test by name | Graded |
| [m02l01-05](m02l01-05/) | Selecting tests by keyword | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: a suite with no configuration

1. In an empty directory, write one module and one test file, and run pytest with no flags.
2. Run it again with the verbose flag, then copy one identifier back to run a single test.
3. Rename the test function so it no longer starts with test, and watch it vanish.

> **Hint:** The collected count in the header is the number to watch while you do this.

## Check yourself

- What two naming rules decide whether pytest collects a test?
- What does deselected mean, and how does it differ from skipped?
- Why must a test class not define a constructor?
- Which flag prints the full identifier of every test?
- How do you assert that a call raises a particular error?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
