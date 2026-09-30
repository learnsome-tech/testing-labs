# m02l04-02 · The module these tests are about

**Lesson:** [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) (lesson 2.4, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can name tests so that a failure summary reads as a sentence, and use those names to select subsets of the suite from the command line.

In the lesson: The discount function again, unchanged, because this lesson changes nothing except the names of the tests around it. That is worth saying out loud: renaming tests is the cheapest improvement available to you. It needs no design decision, it cannot break production, it can be done while you wait for a build, and it improves every future failure report of every test you touch. Keep this function on screen in your head while the names change underneath it, and judge each version by one question: could somebody on call understand the failure without reading this file?

## Files

- [`starter/discount.py`](starter/discount.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/discount.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the discount function again

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
