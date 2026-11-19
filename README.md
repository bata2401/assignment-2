Assignment 2 – Testing AI with Unittest
Introduction

I tested the ask_capital function with Python unittest and Ollama, using the Gemma 4 model. The goal was to check whether the AI gives correct and consistent answers.

Tests
Unknown model: returns “Failure.” if the model doesn’t exist.
Sweden: asks three times; at least two answers must contain Stockholm.
Australia: asks three times; at least two answers must contain Canberra.
Judge accepts: the judge should accept Stockholm as the capital of Sweden.
Judge rejects: the judge should reject a made-up capital for a fictional country.
Test results

I ran the tests five times, and all five tests passed every time.

Run	Passed	Failed
1–5	5	0
Reflections

The model gave the right capitals in every run. That suggests it’s consistent, but it doesn’t prove it will always be right.

The judge also worked as expected. Since the judge is an AI too, it can make mistakes, so when a test fails it’s hard to tell whether the problem is the model or the judge. I used Gemma 4 for both, so they may share the same weaknesses.

I learned that AI answers aren’t fully predictable. That makes testing AI different from testing normal software, and it means you shouldn’t rely on just one test or one AI judge.