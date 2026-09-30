# m01l02-04 · Somebody changes the rate

**Lesson:** [Arrange, Act, Assert](https://learnsome.tech/learn/testing-course/m01l02) (lesson 1.2, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can write a test in three visible phases, and you can show that the phases make the failure report easier to read than a one line test.

In the lesson: Now a realistic accident. A new market needs a higher rate, and somebody edits the default instead of passing the rate in at the call site. The default rate moves from twenty to twenty five per cent. Leave the rest alone: the arithmetic is still correct, the rounding is still correct, and no reviewer reading this diff on its own would object. The only thing wrong is that every caller who relied on the old default is now quietly charging more. Our test claimed a number for the old default, so our test is about to earn its keep twice over: once by failing, and once by how it fails.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the default rate
   - Lines 7–8: leave the rest alone

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
