# m03l04-04 · Randomness with a supplied generator

**Lesson:** [Testing Time And Randomness](https://learnsome.tech/learn/testing-course/m03l04) (lesson 3.4, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can make time and randomness explicit dependencies, freeze them in pytest, and test boundary behaviour without sleeps or lucky seeds.

In the lesson: Randomness deserves the same treatment. This function takes a generator, defaulting to the standard random module for production. A test can supply a tiny object whose choice method returns a known value. That is more useful than seeding the global generator, because a seed couples the test to the number and order of every random call. A supplied generator also lets you test a failure or an empty collection without waiting for chance to select it.

## Files

- [`starter/invite.py`](starter/invite.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/invite.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: takes a generator

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
