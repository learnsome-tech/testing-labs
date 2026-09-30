# m02l02 · Parametrised Tests

Module 2: Unit Testing In Practice · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m02l02)

**Goal:** You can check one claim against many examples with a parametrised test, give each case a readable identifier, and say when cases should be separate tests instead.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | The version that truncates | Read along |
| [m02l02-03](m02l02-03/) | Four cases, one body | Graded |
| [m02l02-04](m02l02-04/) | Giving each case a name | Graded |
| [m02l02-05](m02l02-05/) | Rounding, properly | Read along |
| [m02l02-06](m02l02-06/) | Every case, by name | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: find the awkward cases

1. Take a function of yours with numeric or text input and list its awkward inputs.
2. Parametrise one test over them, with an identifier per case, and run it verbosely.
3. Add a case that fails today and mark it expected to fail, rather than deleting it.

> **Hint:** Awkward means empty, zero, one, negative, the boundary, and one past the boundary.

## Check yourself

- Why is a loop inside one test worse than four parametrised cases?
- What do you gain by writing your own case identifiers?
- When should two cases be separate tests instead of two rows of data?
- Which two signs suggest a parametrised test is doing two jobs?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
