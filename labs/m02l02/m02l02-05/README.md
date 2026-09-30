# m02l02-05 · Rounding, properly

**Lesson:** [Parametrised Tests](https://learnsome.tech/learn/testing-course/m02l02) (lesson 2.2, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can check one claim against many examples with a parametrised test, give each case a readable identifier, and say when cases should be separate tests instead.

In the lesson: Fix the function so that it rounds to the nearest penny. Worth a note in passing, because it catches people out: Python rounds a value sitting exactly halfway to the nearest even number, not always upwards, and in money that is a deliberate decision somebody in finance may have opinions about. For our purposes the important thing is that the behaviour is now defined by the tests rather than by whichever examples a developer happened to try, and the awkward cases are written down in the suite forever.

## Files

- [`starter/discount.py`](starter/discount.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/discount.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: rounds to the nearest penny

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
