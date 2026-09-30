# m02l03-06 · A fixture that cleans up after itself

**Lesson:** [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) (lesson 2.3, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

In the lesson: Teardown is the other half of a fixture, and pytest spells it with yield. Everything before the yield is setup. The value you yield is what the test receives. Everything after it runs when the test is finished, whether that test passed, failed or raised, which is what makes it safe for closing files, dropping tables and stopping containers. A fixture written this way reads in the order it happens, top to bottom, which is easier to trust than a pair of setup and teardown methods a hundred lines apart.

## Files

- [`starter/conftest.py`](starter/conftest.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/conftest.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: everything before the yield
   - Lines 8–9: everything after it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
