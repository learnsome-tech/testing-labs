# m03l04-02 · An expiry check with a clock seam

**Lesson:** [Testing Time And Randomness](https://learnsome.tech/learn/testing-course/m03l04) (lesson 3.4, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can make time and randomness explicit dependencies, freeze them in pytest, and test boundary behaviour without sleeps or lucky seeds.

In the lesson: This expiry check accepts an optional instant called now. Production callers can omit it and use the real UTC clock. Tests can pass a fixed instant and examine the boundary without sleeping. The comparison is strict, so a session is inactive at the exact expiry time. That is a policy choice worth naming in a test. The seam is small, visible and local, and it avoids a global clock patch that could affect unrelated code in the same process.

## Files

- [`starter/session.py`](starter/session.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/session.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: accepts an optional instant
3. Notes from the lesson:
   - Line 5: The optional clock makes the moving input explicit

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
