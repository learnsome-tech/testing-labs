# m02l02-02 · The version that truncates

**Lesson:** [Parametrised Tests](https://learnsome.tech/learn/testing-course/m02l02) (lesson 2.2, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can check one claim against many examples with a parametrised test, give each case a readable identifier, and say when cases should be separate tests instead.

In the lesson: Here is the discount function with one character changed from the version you saw a moment ago: it truncates towards zero instead of rounding. This is an extremely common real bug, because truncation looks like rounding on every example a developer tries by hand. A thousand pence with a tenth off is nine hundred either way. It takes a price where the answer falls on a fraction of a penny before the two behaviours part company, and choosing those prices deliberately is exactly what parametrising is for.

## Files

- [`starter/discount.py`](starter/discount.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/discount.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: truncates towards zero

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
