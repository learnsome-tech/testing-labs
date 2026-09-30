# m04l02-04 · A disposable database fixture

**Lesson:** [Integration Testing With Containers](https://learnsome.tech/learn/testing-course/m04l02) (lesson 4.2, module 4: Testing Time, Files And Services) · Pro  
**Check:** Read along

## Goal

You can decide when an integration test needs a real dependency, start it with a disposable container, and keep the test boundary explicit.

In the lesson: This is the fixture shape, shown as a fragment because the container library call is not installed here. The fixture starts one pinned image, yields a connection to the test, and stops it after the assertion even when the assertion fails. The health check and image wait belong inside start postgres image. In a real project you would use the library for your language, such as Testcontainers Python, and keep the same ownership and cleanup.

## Files

- [`starter/test_db.py`](starter/test_db.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/test_db.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–12: starts one pinned image

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
