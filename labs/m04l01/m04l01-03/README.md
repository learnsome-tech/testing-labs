# m04l01-03 · Move the clock behind a seam

**Lesson:** [Flaky Tests And How To Kill Them](https://learnsome.tech/learn/testing-course/m04l01) (lesson 4.1, module 4: Testing Time, Files And Services) · Pro  
**Check:** Read along

## Goal

You can identify a flaky test, reproduce the moving input, and replace timing luck with a deterministic boundary.

In the lesson: The repair is to move the clock behind a seam. Production still uses the real UTC clock when no instant is supplied. A test supplies the instant it wants, so the assertion describes a rule rather than a scheduling accident. The same pattern works for queues, random sources and filesystem paths: identify the moving input and accept it from the caller.

## Files

- [`starter/clocked.py`](starter/clocked.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/clocked.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: move the clock behind a seam

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
