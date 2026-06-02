# Variables and Algebra

> A variable is a box that holds a number you do not know yet. Algebra is the rule for opening the box: undo each operation, the same on both sides.

**Type:** Learn
**Languages:** Python
**Prerequisites:** The Four Operations and Order (00-13)
**Time:** ~40 minutes

## Learning Objectives

- Read a letter like `x` as "the unknown number" and an equation as a balance
- Solve for `x` by undoing operations in reverse order, doing the same to both sides
- Use the inverse pairs (+ undoes -, x undoes /) from the earlier lessons
- Rearrange the roofline throughput formula to solve for any of its parts

## The Concept

A **variable** is just a name for a number you have not found yet. We usually write it as a letter, like `x`. Nothing mysterious: `x + 3 = 10` is the sentence "some number, plus 3, equals 10". Your job is to find the number.

### An equation is a balance

The `=` sign means "the left side weighs exactly the same as the right side". That gives you the one golden rule of algebra:

> **Whatever you do to one side, you must do to the other.** The balance stays level.

### Solving = undoing operations

To get `x` alone, peel away whatever is attached to it, using the inverse operations you already built:

- addition is undone by subtraction (and the reverse)
- multiplication is undone by division (and the reverse)

Worked example, fully:

```
x + 3 = 10
```

`x` has a `+3` stuck to it. Undo it by subtracting 3 from BOTH sides:

```
x + 3 - 3 = 10 - 3
x = 7
```

Check by putting 7 back in: `7 + 3 = 10`. Correct. Always check; it is free.

A second example with multiplication:

```
4 x = 20      (4 times x is 20)
```

`x` is multiplied by 4. Undo it by dividing BOTH sides by 4:

```
4x / 4 = 20 / 4
x = 5
```

Check: `4 x 5 = 20`. Correct.

### Undo in reverse order

When several things are attached to `x`, undo them in the reverse of the order of operations. Peel the outer layer first.

```
2x + 1 = 9
```

The `+1` is the outer layer, so undo it first (subtract 1 from both sides), then undo the `x2` (divide both sides by 2):

```
2x + 1 - 1 = 9 - 1   ->   2x = 8
2x / 2 = 8 / 2        ->   x = 4
```

Check: `2 x 4 + 1 = 9`. Correct.

### Worked example: the roofline formula

NeuroGrid's inference speed has a ceiling set by memory bandwidth. A simplified roofline says:

```
tokens_per_second = bandwidth / (bytes_per_weight x num_weights)
```

That is fine if you want the speed. But suppose you know the target speed and want to find the `bytes_per_weight` you can afford. Solve for it. The denominator is multiplied into the bottom, so first multiply both sides by the denominator, then divide:

```
tokens_per_second x (bytes_per_weight x num_weights) = bandwidth
bytes_per_weight x num_weights = bandwidth / tokens_per_second
bytes_per_weight = bandwidth / (tokens_per_second x num_weights)
```

Same equation, rearranged to answer a different question. This is exactly why pushing `bytes_per_weight` down from 2 (FP16) toward `0.266` (ternary) raises `tokens_per_second`: a smaller denominator means a bigger result. Algebra is what lets you see which knob moves which number, and by how much.

## Active recall

Produce the answer. Easiest first.

1. Solve `x + 5 = 12`.
2. Solve `3x = 21`.
3. Solve `2x + 4 = 14`.

Answers: `x = 7`; `x = 7`; `x = 5` (subtract 4 to get 2x = 10, then divide by 2).

### Misconception callout

The trap is changing only one side. If you subtract 3 from the left of `x + 3 = 10` but not the right, you get `x = 10`, which is wrong (`10 + 3` is not 10). The balance must stay level: every operation hits BOTH sides, always. Write the operation under both sides so you never forget one.

## Build It

```python
python phases/00-setup-and-tooling/21-variables-and-algebra/code/algebra.py
```

## Why this matters for AI

Every formula in machine learning is an equation with knobs you rearrange: loss as a function of weights, throughput as a function of bandwidth and bit-width, learning rate as a function of step. Training is literally an algorithm for solving for the weights that make the loss smallest. Being able to isolate any variable, and to see that a smaller denominator gives a bigger result, is the daily reasoning of an AI engineer.
