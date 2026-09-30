# m03l05-04 · Missing input is a deliberate case

**Lesson:** [Testing The Filesystem](https://learnsome.tech/learn/testing-course/m03l05) (lesson 3.5, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can test filesystem behaviour with pytest temporary paths, assert the visible file contract, and avoid leaking state between tests.

In the lesson: Now add the read side and make the missing file policy explicit. The reader returns nothing when the path does not exist, otherwise it reads the same encoding the writer used. A missing file is not an exceptional test setup to skip over. It is an input your service must decide how to handle. Because the path is supplied by the caller, the test can point at a fresh directory and know the file is genuinely absent.

## Files

- [`starter/report.py`](starter/report.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–12: returns nothing when the path does not exist

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
