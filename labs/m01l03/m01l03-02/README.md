# m01l03-02 · Code with two bugs in it

**Lesson:** [One Assertion Per Reason](https://learnsome.tech/learn/testing-course/m01l03) (lesson 1.3, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can split a test so that each one fails for exactly one reason, and you can explain why the first failing assertion hides every assertion after it.

In the lesson: Here is the pricing module again, this time as we inherited it, with two separate mistakes. The default rate is wrong: it is the old rate from years ago, not the current one. And the conversion to a whole number of pence truncates instead of rounding, so every price that lands on a fraction of a penny quietly loses that fraction. Two bugs, in two different lines, for two different reasons. Keep that in mind, because how many of them you find out about in one run is entirely a question of how you arranged your assertions.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the default rate is wrong
   - Lines 7–8: truncates instead of rounding

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
