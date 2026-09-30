# m01l05-02 · A function with branches

**Lesson:** [Coverage: Diagnostic, Not Target](https://learnsome.tech/learn/testing-course/m01l05) (lesson 1.5, module 1: What A Test Is For) · Pro  
**Check:** Read along

## Goal

You can read a coverage report to find untested branches, and you can demonstrate a suite with full coverage that fails to notice a live bug.

In the lesson: Here is a function with something to cover. It works out what to hand back for a returned order, it refuses an impossible refund by raising, and it takes an optional restocking fee off the top. Three paths through seven lines: the ordinary path, the guarded error, and the fee. A refund function is a good example on purpose, because getting it wrong costs real money in both directions and because the fee path is exactly the sort of thing a team forgets to test until an accountant notices.

## Files

- [`starter/refund.py`](starter/refund.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/refund.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: refuses an impossible refund
   - Lines 5–7: restocking fee off the top
3. Notes from the lesson:
   - Line 3: A guard clause: one branch that should never be taken in normal use

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
