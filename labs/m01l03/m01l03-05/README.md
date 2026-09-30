# m01l03-05 · A function that returns several things

**Lesson:** [One Assertion Per Reason](https://learnsome.tech/learn/testing-course/m01l03) (lesson 1.3, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can split a test so that each one fails for exactly one reason, and you can explain why the first failing assertion hides every assertion after it.

In the lesson: Now the case where grouping is right. The two broken functions stay exactly as they are, and a new one joins them: quote, which returns the whole calculation as one dictionary, so a customer can see the net, the tax and the total. Three values, but one behaviour. If quote gets the net wrong, everything it returns is wrong together, because they are all derived from the same arithmetic in the same call. That is the test for whether assertions belong in one test: not how many there are, but whether they can fail for unrelated reasons.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the two broken functions
   - Lines 9–15: one dictionary

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
