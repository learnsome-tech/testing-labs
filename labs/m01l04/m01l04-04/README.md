# m01l04-04 · The module both layers touch

**Lesson:** [The Test Pyramid And Where It Is Wrong](https://learnsome.tech/learn/testing-course/m01l04) (lesson 1.4, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can explain what the test pyramid is really a picture of, mark the slow tests in your suite, and select or deselect them by marker.

In the lesson: The same two functions as before, with the rate put back to the current one. The point of showing them again is that the two layers we are about to run are both about this module. One tests the arithmetic directly. The other pretends to call a pricing service that happens to be slow, which is exactly the trade the pyramid is describing: the same behaviour, checked twice, at two very different prices. Nothing about the code changes between the layers. What changes is how much of the world has to be standing up for the check to happen at all.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the same two functions

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
