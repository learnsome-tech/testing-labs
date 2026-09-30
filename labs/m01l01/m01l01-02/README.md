# m01l01-02 · The function under test

**Lesson:** [The Cost And Value Of A Test](https://learnsome.tech/learn/testing-course/m01l01) (lesson 1.1, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can say what a test buys you and what it costs to keep, and you can watch a test catch a regression the moment somebody introduces it.

In the lesson: Here is the code under test: a function called total. It takes a list of cart lines, where every line is a price in pence and a count, and it works out what the customer owes. One expression, no branches, nothing clever. That is deliberate. If you cannot describe what a function should do in a single sentence, you will not be able to write a test that says anything useful about it. Read the docstring, then read the body, and notice that the two of them agree. When they stop agreeing, you have either a bug or a stale comment, and a test is how you find out which.

## Files

- [`starter/cart.py`](starter/cart.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cart.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: a function called total
   - Lines 2–3: one expression

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
