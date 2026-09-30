# m03l01-02 · The dependency we cannot call

**Lesson:** [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) (lesson 3.1, module 3: Test Doubles And Boundaries) · Pro  
**Check:** Read along

## Goal

You can explain the four reasons to replace a collaborator in a test, introduce a seam by passing it in, and test an error path the real dependency will not produce on demand.

In the lesson: Here is the collaborator. An error type the gateway raises when it does not answer in time, and the real client, whose charge method takes an amount in pence and a reference. In this course the real client never runs in a test, and the body says so out loud rather than pretending. In your codebase the body would be an HTTP call with a secret key and a timeout. Every reason from the previous panel applies to it at once: slow, not ours, not deterministic, and impossible to make fail on demand.

## Files

- [`starter/gateway.py`](starter/gateway.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/gateway.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: an error type
   - Lines 4–9: the real client
3. Notes from the lesson:
   - Line 9: In a test this would reach the network, so it never runs here

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
