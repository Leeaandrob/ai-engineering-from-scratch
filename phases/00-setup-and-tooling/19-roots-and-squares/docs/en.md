# Roots and Squares

> A root is the counting flip of a power. A square root asks: what number, multiplied by itself, gives this?

**Type:** Learn
**Languages:** Python
**Prerequisites:** Powers and Exponents (00-17)
**Time:** ~35 minutes

## Learning Objectives

- Read a square root as the inverse of squaring
- Estimate `sqrt(2)` and know it is about `1.414`
- Connect a fractional exponent like `2^1.5` to a root (it is `2 x sqrt(2)`)
- Compute the length of a small vector with the Pythagorean formula

## The Concept

In lesson 00-16 you met the counting flip: every operation has an inverse that runs it backwards. A **root** is the inverse of a **power**.

### Squaring and its inverse

To **square** a number is to raise it to the power 2, which is to multiply it by itself:

```
3^2 = 3 x 3 = 9     "3 squared is 9"
```

The **square root** runs that backwards. It asks: "what number, multiplied by itself, gives 9?"

```
sqrt(9) = 3     because 3 x 3 = 9
```

The symbol `sqrt(x)` (the radical sign) means "the square root of x". Squaring and square-rooting undo each other, exactly like `+` and `-`, or `x` and `/`.

```
4^2 = 16    <-->    sqrt(16) = 4
5^2 = 25    <-->    sqrt(25) = 5
```

### Not every root is a whole number

`sqrt(9) = 3` is clean because 9 is a perfect square. But what is `sqrt(2)`? There is no whole number that squares to 2: `1 x 1 = 1` (too small) and `2 x 2 = 4` (too big). So `sqrt(2)` lives between 1 and 2. Its value is:

```
sqrt(2) = 1.41421...   about 1.414
```

Check it: `1.414 x 1.414 = 1.9994`, just under 2. This is one of the most common numbers in all of machine learning.

### A root is a fractional exponent

Here is the bridge back to lesson 00-17. A square root is the same as raising to the power `1/2`:

```
sqrt(2) = 2^(1/2) = 2^0.5 = 1.414
```

That looks strange, but it follows from the rules of exponents: `2^0.5 x 2^0.5 = 2^(0.5+0.5) = 2^1 = 2`, so `2^0.5` is the thing that squares to 2, which is the square root. This unlocks fractional exponents in general. For example:

```
2^1.5 = 2^1 x 2^0.5 = 2 x sqrt(2) = 2 x 1.414 = 2.83
```

Hold onto `2^1.5 = 2 x sqrt(2) = 2.83`. The keystone logarithm lesson (00-20) uses exactly this fact to explain a number that surprises everyone.

### Worked example: the length of a vector

A vector with components `3` and `2` is an arrow that goes 3 right and 2 up. Its length is found with the Pythagorean idea: square each component, add, then take the square root.

```
length = sqrt(3^2 + 2^2) = sqrt(9 + 4) = sqrt(13) = 3.606
```

Watch the order of operations from lesson 00-13: the powers happen first, then the addition inside the root, then the root last. This `sqrt(sum of squares)` pattern is how every distance and every vector magnitude in this course is computed.

## Active recall

Produce the answer. Easiest first.

1. `sqrt(25)` = ?
2. `sqrt(2)` is about ?
3. `sqrt(3^2 + 4^2)` = ?

Answers: `5`; about `1.414`; `5` (sqrt(9+16) = sqrt(25) = 5).

### Misconception callout

The trap is reading `sqrt(a + b)` as `sqrt(a) + sqrt(b)`. They are not equal. `sqrt(9 + 16) = sqrt(25) = 5`, but `sqrt(9) + sqrt(16) = 3 + 4 = 7`. The root applies to the whole sum at once, after the addition inside is done. The radical sign acts like an invisible pair of parentheses.

## Build It

```python
python phases/00-setup-and-tooling/19-roots-and-squares/code/roots.py
```

## Why this matters for AI

Vector length, distance between embeddings, the normalization inside attention, the `1/sqrt(d)` scaling factor in transformers, the root in root-mean-square layer norm: all of them are square roots. The `sqrt(sum of squares)` pattern is the single most common geometric operation in deep learning, and the fractional-exponent view (`x^0.5`) is what lets the next lesson explain the "1.58-bit" number precisely.
