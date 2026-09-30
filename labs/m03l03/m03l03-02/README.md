# m03l03-02 · A bug hidden by a mock

**Lesson:** [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) (lesson 3.3, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can spot a test that only verifies its mock script, replace brittle interaction checks with a behavioural seam, and make a broken system fail for the right reason.

In the lesson: Here is a tiny bug hiding in plain sight. The payment function calls the gateway and returns a field named ID. The gateway contract in this course returns a field named reference. A mock can hide that mismatch if the test teaches the mock to return an ID as well. The production path will raise a key error after a successful charge, which is a particularly expensive kind of failure. The code is short enough to read in one breath, and the missing contract is exactly why a green mock test is not evidence by itself.

## Files

- [`starter/checkout.py`](starter/checkout.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/checkout.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: returns a field named id

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
