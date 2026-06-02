# Repeated Operations and the Counting Flip

> Multiplication is just addition done over and over. Once you see that, you can ask a brand new question: how many times did I repeat?

**Type:** Learn
**Languages:** Python
**Prerequisites:** The Four Operations and Order (00-13)
**Time:** ~35 minutes

## Learning Objectives

- See multiplication as repeated addition
- Perform the "counting flip": instead of doing an operation, count how many times it was done
- Build the doubling ladder 1 -> 2 -> 4 -> 8 -> 16 and count the steps
- Set up the mental move that makes exponents (00-17) and logarithms (00-20) easy

## The Concept

This lesson teaches a way of thinking, not a new symbol. It is the hinge the whole phase turns on.

### Multiplication is repeated addition

You learned `x` as its own operation, but it is a shortcut for adding the same number again and again:

```
3 x 4   =   3 + 3 + 3 + 3   =   12
```

"3 times 4" means "add 3, four times". The `4` is not a thing you add. The `4` is a **count**: how many copies of 3 you piled up. Hold that thought. The number that tells you "how many times" is a different kind of number from the thing being repeated.

### The counting flip

Here is the move. Normally you are handed the pieces and asked for the total:

```
add 3, four times   ->   what is the total?   ->   12
```

The flip turns the question inside out. You are handed the total and asked for the count:

```
I kept adding 3 and reached 12   ->   how many times did I add?   ->   4
```

Same situation, opposite question. The first asks "what do I get?". The flip asks "how many repetitions got me there?". Every inverse operation in math is a counting flip of this kind. Subtraction is the flip of addition. Division is the flip of multiplication ("how many 3s fit into 12?" is `12 / 3 = 4`). And later, the logarithm will be the flip of the exponent.

### The doubling ladder

The most important repetition in this whole curriculum is **doubling**: multiplying by 2 over and over. Start at 1 and keep doubling:

```
start:   1
double:  1 x 2 = 2     (1 step)
double:  2 x 2 = 4     (2 steps)
double:  4 x 2 = 8     (3 steps)
double:  8 x 2 = 16    (4 steps)
```

Read the ladder two ways:

- **Forward (the operation):** "double 3 times starting from 1" lands on `8`.
- **Flipped (the count):** "I doubled from 1 and reached 8, how many doublings was that?" The answer is `3`.

That second question, counting the doublings, is exactly what a logarithm is. We are building it now, four lessons early, so that when it arrives it is old news.

## Active recall

Produce the answer. Easiest first.

1. Write `5 x 3` as a repeated addition, then give the total.
2. Start at 1 and double 4 times. Where do you land?
3. I doubled from 1 and landed on 16. How many times did I double?

Answers: `5 + 5 + 5 = 15`; `1 -> 2 -> 4 -> 8 -> 16`, lands on `16`; `4` doublings (count the arrows).

### Misconception callout

Critical trap, and it returns in the logarithm lesson: **doing one division is NOT the same as counting repetitions.** "How many times did I double to reach 8?" is not `8 / 2 = 4`. Dividing by 2 once just undoes a single doubling (8 back to 4). To count the doublings you have to step down the ladder repeatedly (8 -> 4 -> 2 -> 1) and count the steps, which is `3`. One operation versus a count of operations: keep them separate.

## Build It

```python
python phases/00-setup-and-tooling/16-repeated-operations/code/repeated.py
```

## Why this matters for AI

Model sizes, memory, and learning rates all move by doubling and halving, not by adding. "Twice the context", "half the precision", "the model is 2^10 = 1024 times bigger": these are all rungs on a doubling ladder. The counting flip you practiced here is the single idea behind exponents, scientific notation, and the keystone logarithm lesson that defines the "1.58-bit" name of the whole project.
