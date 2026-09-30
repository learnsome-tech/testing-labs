# m02l03-02 · Two fixtures, two scopes

**Lesson:** [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) (lesson 2.3, module 2: Unit Testing In Practice) · Pro  
**Check:** Read along

## Goal

You can write a fixture with setup and teardown, choose its scope deliberately, and recognise the shared-state bug a wide scope invites.

In the lesson: Fixtures live in a file called conftest dot py, which pytest loads automatically for every test in that directory and below, with no import. The first fixture is the default, function scope: a fresh basket for every test that asks. The second one is module scope, so it is built once for every test in the file that asks for it and then reused. Both print something, because in this lesson the order things happen is the whole subject, and printing is the bluntest way to see it.

## Files

- [`starter/conftest.py`](starter/conftest.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/conftest.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: the first fixture
   - Lines 8–13: the second one
3. Notes from the lesson:
   - Line 10: Module scope: built once for every test in the file that asks

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
