# m03l03-05 · Fix the behaviour, then simplify

**Lesson:** [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) (lesson 3.3, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

In the lesson: Fix the implementation by reading the field the contract actually promises, reference. The code gets simpler because the test no longer needs a special mock return value. In a larger service you might put this shape behind a typed adapter, but the principle is unchanged: make the boundary explicit and test the behaviour that crosses it. When a mock and a fake disagree, believe the working contract and make the disagreement visible.

## Files

- [`starter/checkout.py`](starter/checkout.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/checkout.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: reading the field the contract actually promises

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
