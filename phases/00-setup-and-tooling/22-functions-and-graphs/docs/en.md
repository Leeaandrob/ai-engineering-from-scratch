# Functions and Graphs

> A function is a machine: feed it a number, get a number back. A graph is a picture of every input-output pair at once.

**Type:** Learn
**Languages:** Python
**Prerequisites:** Variables and Algebra (00-21)
**Time:** ~40 minutes

## Learning Objectives

- Read `f(x)` as "the output of the machine f when you feed it x"
- Evaluate a function at a given input
- Recognize the shapes of three functions by intuition: linear, exponential, sigmoid
- Connect each shape to a real AI quantity (a learning-rate line, exponential decay, a sigmoid gate)

## The Concept

### A function is an input-output machine

In lesson 00-21 a variable was an unknown to solve for. A **function** is different: it is a rule that turns any input into an output. We write it `f(x)`, read "f of x", meaning "the value the machine f produces when fed x".

```
f(x) = 2x + 1
```

This machine doubles the input and adds 1. Feed it numbers:

```
f(0) = 2(0) + 1 = 1
f(3) = 2(3) + 1 = 7
f(5) = 2(5) + 1 = 11
```

The `x` is a slot you fill in. The whole right side is just the order-of-operations arithmetic from lesson 00-13, evaluated at whatever you plug in. Note this is NOT solving for x; you are GIVEN x and you compute the output.

### A graph is a picture of the machine

If you compute `f(x)` for many inputs and plot each `(input, output)` pair as a dot, the dots form a shape. That shape is the **graph**, and its shape tells you instantly how the machine behaves. You do not need to draw it perfectly; you need to recognize three shapes.

### Shape 1: linear (a straight line)

```
f(x) = 2x + 1
```

Every step right by 1 moves the output up by the same amount (here, 2). Constant change gives a straight line. The number multiplying `x` (the `2`) is the steepness, called the slope. A learning-rate "warmup" that rises by a fixed amount each step is a line.

### Shape 2: exponential (a curve that explodes or decays)

```
f(x) = 2^x
```

This is the powers lesson (00-17) turned into a function. Each step right does not add a fixed amount; it MULTIPLIES by 2. So the output doubles every step: 1, 2, 4, 8, 16. The curve starts flat and shoots upward. Run it backwards with a negative sign and it decays toward zero instead:

```
f(x) = 2^(-x)     ->   1, 0.5, 0.25, 0.125, ...   (halving each step)
```

Learning-rate decay schedules and the `exp(-x)` weighting in many AI formulas are this shape.

### Shape 3: sigmoid (an S that squashes anything into 0 to 1)

```
sigmoid(x) = 1 / (1 + e^(-x))
```

It looks busy, but its behavior is simple: it takes ANY input, from a huge negative number to a huge positive number, and squashes it into the range between 0 and 1. Very negative input gives almost 0, very positive gives almost 1, and `sigmoid(0) = 0.5` sits exactly in the middle. The curve is a stretched letter S. This is the classic "gate" or "probability" shape: it turns a raw score into something you can read as "how on, from 0 to 1". Neurons, attention gates, and binary classifiers all use it.

### The one-line summary of the three shapes

```
linear:       constant change      ->  straight line
exponential:  multiplying change   ->  flat then explosive (or decaying)
sigmoid:      squashed             ->  S-curve, output trapped in 0..1
```

## Active recall

Produce the answer. Easiest first.

1. For `f(x) = 2x + 1`, what is `f(4)`?
2. For `g(x) = 2^x`, what is `g(3)`?
3. Roughly, what is `sigmoid(0)`, and why?

Answers: `9` (2x4+1); `8` (the doubling ladder, 2^3); `0.5`, because a 0 input lands exactly in the middle of the 0-to-1 range.

### Misconception callout

The trap is confusing linear and exponential growth. A line ADDS the same amount each step; an exponential MULTIPLIES each step. They look similar near the start, but the exponential leaves the line far behind: at x = 10, the line `2x` is 20 while `2^x` is 1024. When someone says "it grows linearly" versus "it grows exponentially", that factor (50x here, and rising) is the whole difference.

## Build It

```python
python phases/00-setup-and-tooling/22-functions-and-graphs/code/functions.py
```

## Why this matters for AI

Models are functions: a network is one enormous `f(inputs) = outputs`. Training reshapes that function to fit data. The three shapes here are everywhere: linear layers do `Wx + b`, learning-rate schedules ramp and decay, and the sigmoid (and its cousin softmax) turns scores into probabilities at the output of nearly every classifier. Recognizing a shape from its formula is how you predict what a piece of a model will do before you ever run it.
