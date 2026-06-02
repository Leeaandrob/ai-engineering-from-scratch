# Summation Notation

> The big Greek Sigma is not scary. It is a shorthand for "add up a list", with a counter that says where to start and where to stop.

**Type:** Learn
**Languages:** Python
**Prerequisites:** Powers and Exponents (00-17)
**Time:** ~35 minutes

## Learning Objectives

- Read the Sigma symbol and its start, stop, and term parts
- Expand a summation into the plain addition it stands for
- Compute a small sum by hand
- Recognize the dot product as a sum of products, the first formula of Phase 1

## The Concept

You already know addition. Summation notation is just a compact way to write a long addition without typing every term.

### The Sigma is a loop you write on paper

The symbol is the Greek capital S, written as Sigma. In plain text we will write it `sum`. A full summation has four parts:

```
        stop
        ___
        \
        /     term(i)
        ---
        i = start
```

Read it as: "for the counter `i` running from `start` up to `stop`, compute `term(i)`, and add all those terms together." It is exactly a loop that accumulates a total, written in one symbol.

### Expanding a sum

The honest way to understand any Sigma is to write out what it stands for. Take:

```
sum from i=1 to 4 of i      =  1 + 2 + 3 + 4  =  10
```

The counter `i` walks 1, 2, 3, 4, and at each step the term is just `i` itself. Add them: 10. That is the whole trick. Another one, where the term squares the counter:

```
sum from i=1 to 3 of i^2    =  1^2 + 2^2 + 3^2  =  1 + 4 + 9  =  14
```

The counter still walks 1, 2, 3, but now each term is `i^2` (using the powers from lesson 00-17). Expand first, then add.

### Summing a list

Most often the term pulls the `i`-th value out of a list. If `a = [10, 20, 30]`, then with `i` running over the positions:

```
sum of a[i]  =  a[1] + a[2] + a[3]  =  10 + 20 + 30  =  60
```

The Sigma just says "add every element of the list".

### Worked example: the dot product

Here is where this lands. The very first formula of Phase 1 (the math foundations phase) is the **dot product** of two lists of numbers `a` and `b`:

```
a . b  =  sum of (a[i] x b[i])
```

In words: walk both lists together, multiply each pair `a[i] x b[i]`, and add up all those products. With `a = [1, 2, 3]` and `b = [4, 5, 6]`:

```
a . b  =  (1 x 4) + (2 x 5) + (3 x 6)  =  4 + 10 + 18  =  32
```

That is it. The dot product is a sum of products, and "sum of products" is exactly what the Sigma notation packs into one symbol. Every neural network multiplies and sums billions of these. The notation you just learned is the language that whole field is written in.

## Active recall

Produce the answer. Easiest first.

1. Expand and compute `sum from i=1 to 3 of i`.
2. Compute `sum from i=1 to 3 of i^2`.
3. For `a = [1, 2, 3]` and `b = [4, 5, 6]`, compute the dot product `sum of a[i] x b[i]`.

Answers: `1 + 2 + 3 = 6`; `1 + 4 + 9 = 14`; `4 + 10 + 18 = 32`.

### Misconception callout

The trap is treating the Sigma as a single mysterious operation instead of a loop you can always expand. When a sum confuses you, write out every term the long way and add them by hand. The notation is shorthand for ordinary addition; it never does anything you could not do with `+` and patience. Also watch the start and stop bounds: "i from 1 to 4" includes both 1 and 4, so it is four terms, not three.

## Build It

```python
python phases/00-setup-and-tooling/23-summation-notation/code/summation.py
```

## Why this matters for AI

Summation is the single most common symbol in machine learning math. Loss functions are sums over training examples. The dot product, sum of products, is the core of every matrix multiply, which is the core of every layer of every network. When you reach Phase 1 and see `a . b = sum a_i b_i` on the first line, it will read as plain addition of products, because you built the Sigma from the four operations yourself.
