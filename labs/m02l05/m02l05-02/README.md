# m02l05-02 · The module under test

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Two tiny functions to break on purpose. One adds up the lines of an invoice. The other pulls out the names in order. They are deliberately trivial, because the subject of this lesson is not the code, it is the report, and a complicated example would put the interesting part of the screen underneath a wall of application logic. Everything you are about to read applies unchanged to a failure in a thousand line service, because pytest builds the report the same way in both cases.

## Files

- [`starter/invoice.py`](starter/invoice.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/invoice.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: adds up the lines
   - Lines 4–8: the names in order

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
