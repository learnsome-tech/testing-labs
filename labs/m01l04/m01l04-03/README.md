# m01l04-03 · Registering a marker

**Lesson:** [The Test Pyramid And Where It Is Wrong](https://learnsome.tech/learn/testing-course/m01l04) (lesson 1.4, module 1: What A Test Is For) · Free  
**Check:** Read along

## Goal

You can explain what the test pyramid is really a picture of, mark the slow tests in your suite, and select or deselect them by marker.

In the lesson: Before we can talk about layers in a real suite, we need a way to say which layer a test is in. In pytest that is a marker, and markers are declared in the configuration file so that a typo becomes an error instead of a test that silently never runs. One line of documentation per marker, in the file, where the next person will find it. The equivalents elsewhere are tags in JUnit, categories in dot net, and the convention of separate directories in Go, but the idea is identical: label the test with what it needs, then choose by label.

## Files

- [`starter/pytest.ini`](starter/pytest.ini): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pytest.ini` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: the configuration file
   - Lines 2–3: one line of documentation

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
