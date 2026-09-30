# m02l04-03 · Names that say nothing

**Lesson:** [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) (lesson 2.4, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can name tests so that a failure summary reads as a sentence, and use those names to select subsets of the suite from the command line.

In the lesson: Here is a real pattern from real codebases. The first two names are numbered, which tells you only that somebody wrote a second test after the first. The third is worse, because the word edge sounds meaningful and is not: an edge of what, in which direction, and what should happen there? The assertions themselves are fine. Every fact you would want is present in the file. The problem is that none of it survives into the report, which is the only place most people will meet these tests.

## Files

- [`starter/discount.py`](starter/discount.py)
- [`starter/test_names.py`](starter/test_names.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/test_names.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the first two names
   - Lines 6–13: the third is worse

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
