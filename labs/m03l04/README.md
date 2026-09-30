# m03l04 · Testing Time And Randomness

Module 3: Test Doubles And Boundaries · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/testing-course/m03l04)

**Goal:** You can make time and randomness explicit dependencies, freeze them in pytest, and test boundary behaviour without sleeps or lucky seeds.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-02](m03l04-02/) | An expiry check with a clock seam | Read along |
| [m03l04-03](m03l04-03/) | Freeze time at both sides of the boundary | Graded |
| [m03l04-04](m03l04-04/) | Randomness with a supplied generator | Read along |
| [m03l04-05](m03l04-05/) | Choose the result on purpose | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: control a moving input

1. Find code that reads the clock or random module directly.
2. Add a seam and test the exact boundary with a fixed input.
3. Add a test for the rare failure or empty case without relying on chance.

> **Hint:** A clock argument or generator argument is often the smallest useful seam.

## Check yourself

- Why does sleeping fail to make a time test reliable?
- What boundary does the expiry example specify?
- Why is an injected generator stronger than a global seed?
- Which name should you patch when injection is impossible?

---

[Course README](../../README.md) · [Automated Testing, TDD & Quality Engineering on LearnSome.tech](https://learnsome.tech/courses/testing-course)
