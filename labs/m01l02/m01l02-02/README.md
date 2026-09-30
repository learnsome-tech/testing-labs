# m01l02-02 · The module we will be pricing with

**Lesson:** [Arrange, Act, Assert](https://learnsome.tech/learn/testing-course/m01l02) (lesson 1.2, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can write a test in three visible phases, and you can show that the phases make the failure report easier to read than a one line test.

In the lesson: Two small functions carry this module. The first adds up the lines of a basket, in pence. The second adds value added tax at a default rate and rounds to the nearest penny. Both are pure: hand them the same arguments and they hand back the same answer, with nothing kept between calls. Pure functions are the easiest thing in the world to test, which is why almost every testing tutorial uses them, and also why almost every testing tutorial leaves you helpless in front of real code. We will earn our way up to clocks, files, containers and other services later in this course. Today, the shape of a test.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: adds up the lines
   - Lines 4–8: adds value added tax

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
