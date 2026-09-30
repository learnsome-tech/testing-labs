# m05l03 · What To Automate Away

Module 5: Quality Gates And Code Review · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m05l03)

**Goal:** You can automate mechanical review work, keep policy visible in tools, and reserve human attention for decisions automation cannot make.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-03](m05l03-03/) | A required check really runs | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: remove one manual check

1. Find one review comment that repeats a mechanical rule.
2. Encode that rule in a formatter, linter or test.
3. Rewrite the review guide to point at the automated result.

> **Hint:** Automate the rule only when the tool can explain a failure and a fix.

## Check yourself

- Which work should be automated?
- Why do false positives damage a gate?
- What cannot a green build prove?
- When should a reviewer keep a question human?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
