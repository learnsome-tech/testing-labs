# m03l02-02 · The interface all four stand in for

**Lesson:** [Fakes, Stubs, Mocks And Spies](https://learnsome.tech/learn/testing-course/m03l02) (lesson 3.2, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can name and write the four kinds of test double, and choose between them by what the test needs to observe.

In the lesson: One method, two parameters, one returned receipt. Everything in this lesson stands in for that. Keeping the interface this small is not a simplification for teaching: it is the practice. A narrow boundary is what makes doubles cheap, and a collaborator with fifteen methods is a collaborator you will end up mocking badly. If your seam is wide, the honest fix is a smaller interface in front of it, defined by what your code needs rather than by everything the vendor offers.

## Files

- [`starter/gateway.py`](starter/gateway.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/gateway.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: one method

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
