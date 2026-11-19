Assignment 2 – Testing AI with Unittest
Introduction

We tested the ask_capital function with Python unittest and Ollama, using the Gemma4 model. The goal was to check whether the AI gives correct and consistent answers

Tests
Unknown model: returns (Failure) if the model doesn’t exist.
Sweden: asks three times; at least two answers must have Stockholm.
Australia: asks three times; at least two answers must have Canberra.
Judge accepts: the judge should accept Stockholm as the capital of Sweden.
Judge rejects: the judge should reject a made-up capital for any country.
Test results

We ran the tests five times, and all five tests passed every time.

| Runs | Passed | Failed |
|:----:|:------:|:------:|
| 1–5  | **5**  | **0**  |

Reflections

The model gave the right capitals in every run. That was consistent, but it doesn’t prove it will always work this way.

The judge also worked as expected. Since the judge is an AI aswell, it can make mistakes, so when a test fails it’s hard to tell whether the problem is the model or the judge. We used Gemma 4 for both, so they may share the same weaknesses.

We learned that AI answers aren’t fully predictable, so one test or one judge isn’t enough.