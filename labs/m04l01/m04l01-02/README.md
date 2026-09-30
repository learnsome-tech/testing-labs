# m04l01-02 · The time dependent test fails for real

**Lesson:** [Flaky Tests And How To Kill Them](https://learnsome.tech/learn/testing-course/m04l01) (lesson 4.1, module 4: Testing Time, Files And Services) · Pro  
**Check:** Read along

## Goal

You can identify a flaky test, reproduce the moving input, and replace timing luck with a deterministic boundary.

In the lesson: Here is a deliberately time dependent test, and it fails for real on this run. It asks the wall clock to be at the first second of a minute, which is almost never true. The exact number in the report is incidental, but the failure is honest: the test reads a moving input and compares it with a fixed story. Do not make this green by trying until the clock happens to agree.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/test_flaky.py`](starter/test_flaky.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/test_flaky.py` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   pytest -q --tb=no test_flaky.py
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
