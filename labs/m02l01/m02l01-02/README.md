# m02l01-02 · The module under test

**Lesson:** [Introducing pytest](https://learnsome.tech/learn/testing-course/m02l01) (lesson 2.1, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can write and run a pytest suite with no configuration, read the session header, and select tests by name from the command line.

In the lesson: One function to work with: it takes a percentage off a price, in pence, and refuses a nonsense percentage by raising instead of returning a number nobody can trust. Two behaviours in five lines, which is the right size for a first suite. Notice the guard comes first and that the happy path is the last line: that shape makes the function easy to describe, and anything easy to describe is easy to test. If you cannot write the docstring, do not start with the test. Write the docstring, then let the tests hold you to it.

## Files

- [`starter/discount.py`](starter/discount.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/discount.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: a percentage off a price
   - Lines 3–5: refuses a nonsense percentage

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
