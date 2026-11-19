# Assignment 2 – Testing AI with Unittest

## Introduction

In this assignment, I tested the ask_capital function using Python unittest and Ollama with the Gemma 4 model. The purpose was to check if the AI gives correct answers and if the results are consistent.

## Tests

I created five tests:

1. Unknown model: checks if the function returns "Failure." when the model does not exist.
2. Sweden: asks for the capital of Sweden three times and checks if at least two answers contain Stockholm.
3. Australia: asks for the capital of Australia three times and checks if at least two answers contain Canberra.
4. LLM-as-a-judge accepts: checks if the judge accepts Stockholm as the capital of Sweden.
5. LLM-as-a-judge rejects: checks if the judge rejects an invented capital for a fictional country.

## Test results

I ran all five tests five times. All tests passed in every run.

| Run | Passed | Failed |
|---|---|---|
| 1 | 5 | 0 |
| 2 | 5 | 0 |
| 3 | 5 | 0 |
| 4 | 5 | 0 |
| 5 | 5 | 0 |

## Reflections

The results were the same in all five runs. The model always gave the correct capitals for Sweden and Australia in my tests.

I think consistency tests are useful because they show if the model can give the same correct answer several times. However, passing the tests does not mean that the AI will always be correct.

I also tested LLM-as-a-judge. The judge accepted the correct answer for Sweden and rejected the invented capital for Bealandia. But the judge is also an AI model, so it can make mistakes too.

If a test fails, it can be difficult to know if the problem comes from the model being tested or from the judge. For example, the first model could give a correct answer but the judge could reject it. It is also possible that the judge accepts an incorrect answer.

In my tests, I used Gemma 4 for both generating answers and judging them. This means they can have similar weaknesses. Using another model as a judge could help, but it would not guarantee correct results.

Overall, I learned that testing AI is different from testing normal software because AI answers are not always predictable. We should not depend only on one test or one AI judge.