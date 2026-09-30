# m02l05-05 · A module that returns floats

**Lesson:** [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) (lesson 2.5, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can read a pytest failure report part by part, use approximate comparison for floats, and add a message that tells the reader what the numbers meant.

In the lesson: Money and floats, which is where confident assertions go wrong. This module refuses an unknown currency by raising a key error that names the currency, and otherwise multiplies by a rate. Nothing here is unusual, and that is the point: as soon as a test asserts on the result of floating point arithmetic, exact equality becomes a coin toss that depends on the values. In production code you would keep money in integer pence or a decimal type. In a test, you need a comparison that tolerates the last bit.

## Files

- [`starter/rates.py`](starter/rates.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/rates.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–9: refuses an unknown currency
   - Lines 10–13: multiplies by a rate

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
