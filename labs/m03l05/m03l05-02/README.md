# m03l05-02 · Write a report to a supplied directory

**Lesson:** [Testing The Filesystem](https://learnsome.tech/learn/testing-course/m03l05) (lesson 3.5, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can test filesystem behaviour with pytest temporary paths, assert the visible file contract, and avoid leaking state between tests.

In the lesson: This writer takes its destination folder as an argument and returns the path it wrote. The caller chooses the directory, so a test can choose a temporary one. Path joins the folder and the file name without string concatenation, and write text pins the encoding. These details are small, but they are part of the contract. The function does not know whether the folder is a home directory, a container mount or a pytest temporary path, which keeps the production code independent of the test harness.

## Files

- [`starter/report.py`](starter/report.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: returns the path it wrote
3. Notes from the lesson:
   - Line 5: The caller chooses the directory, so tests do too

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
