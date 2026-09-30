# m03l01-03 · A seam: pass the collaborator in

**Lesson:** [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) (lesson 3.1, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

In the lesson: Now the code under test. The gateway arrives as an argument rather than being constructed inside, and that is the whole trick: the seam. Two outcomes, and both matter. A successful charge gives back the reference the gateway confirmed. A timeout is caught and reported as nothing to show the customer. If this function had built its own gateway, there would be no way to test either path without a network, and the only remaining option would be patching the module from the outside, which is where mocking goes wrong. Injection first, patching only when injection is impossible.

## Files

- [`starter/checkout.py`](starter/checkout.py): the listing from the lesson
- [`starter/gateway.py`](starter/gateway.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/checkout.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the gateway arrives as an argument
   - Lines 6–10: two outcomes
3. Notes from the lesson:
   - Line 4: The seam: whatever is passed in is what gets called

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
