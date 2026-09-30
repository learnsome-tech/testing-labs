# m02l03 · Fixtures And Their Scope

Module 2: Unit Testing In Practice · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m02l03)

**Goal:** You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | Two fixtures, two scopes | Read along |
| [m02l03-03](m02l03-03/) | Watching the scopes fire | Graded |
| [m02l03-05](m02l03-05/) | A wide scope that leaks | Graded |
| [m02l03-06](m02l03-06/) | A fixture that cleans up after itself | Read along |
| [m02l03-07](m02l03-07/) | Setup and teardown, in order | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: narrow a scope and see what breaks

1. Find a module or session scoped fixture in your suite that is not read only.
2. Narrow it to function scope, run the suite, and note which tests now fail.
3. For each failure, decide whether the test or the shared state was the real bug.

> **Hint:** Run the suite in a different order too: reordering is how these bugs are usually found.

## Check yourself

- How does a test say which fixtures it needs?
- What runs after the yield in a fixture, and when?
- Give the one good reason to widen a fixture beyond function scope.
- Why does a shared mutable fixture make failures move around?
- Which file do fixtures go in so that no test has to import them?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
