# Powers and Exponents

> If multiplication is repeated addition, an exponent is repeated multiplication. The little raised number is a count of how many times you multiply.

**Type:** Learn
**Languages:** Python
**Prerequisites:** Repeated Operations and the Counting Flip (00-16)
**Time:** ~35 minutes

## Learning Objectives

- Read `2^10` as "multiply 2 by itself, ten times" and compute small powers by hand
- Connect the exponent to the doubling count from lesson 00-16
- Use powers of two to reason about bits, bytes, and model sizes
- Explain why 16 bits = 2 bytes, why a 2-bit code has 4 values, and what 2^10 = 1024 means

## The Concept

Lesson 00-16 gave you the ladder of moves. Here is the symbol for it.

### An exponent is repeated multiplication

Multiplication was repeated addition. Take the exact same idea up one floor: an **exponent** is repeated multiplication.

```
2^3   =   2 x 2 x 2   =   8
```

Read `2^3` as "2 to the power 3" or "2 multiplied by itself 3 times". The big number on the bottom (`2`) is the **base**, the thing being multiplied. The small raised number (`3`) is the **exponent**, the count of how many times. This is the doubling ladder from last lesson: doubling 3 times from 1 lands on 8, and `2^3 = 8`. Same thing, now with a symbol.

```
2^1 = 2
2^2 = 2 x 2 = 4
2^3 = 2 x 2 x 2 = 8
2^4 = 2 x 2 x 2 x 2 = 16
```

Each step up the exponent doubles the result. The exponent IS the count of doublings.

### Two anchors you must know

```
2^10 = 1024     "about a thousand", the jump from one size class to the next
2^0  = 1        anything to the power 0 is 1 (you multiplied zero times, you are still at the start)
```

`2^0 = 1` looks strange until you remember the ladder starts at 1. Zero doublings means you never left 1.

### Worked example: bits, bytes, and codes

A **bit** is one slot that is either 0 or 1, so it has `2^1 = 2` possible values. Add a second bit and you can make 00, 01, 10, 11: that is `2^2 = 4` values. Each extra bit doubles the number of patterns:

```
1 bit  -> 2^1 = 2 values
2 bits -> 2^2 = 4 values   (a "2-bit code" stores one of 4 things)
8 bits -> 2^8 = 256 values (this is one byte)
```

So a **byte** (8 bits) holds `2^8 = 256` distinct values. And a 16-bit number (FP16, a common weight format) uses 16 bits, which is `16 / 8 = 2` bytes. That is where the "2 bytes per weight" from lesson 00-14 came from.

Now the project anchor. A NeuroGrid model has roughly `2^10 = 1024` thousand-blocks worth of weights, and the full FP16 version weighs about `1.75` GB. Cutting each weight from 16 bits toward the ternary `log2(3)` bits (the next lessons build that number) is what shrinks `1.75` GB down to something that fits on a single small device.

## Active recall

Produce the answer. Easiest first.

1. `2^2` = ?
2. `2^5` = ?
3. How many distinct values can a 2-bit code store?

Answers: `4`; `32` (2x2x2x2x2); `4` (which is `2^2`).

### Misconception callout

The trap is swapping the base and the exponent. `2^3` is `2 x 2 x 2 = 8`, NOT `3 x 3 = 9` and NOT `2 x 3 = 6`. The base is the number you repeat; the exponent only counts the repeats. When the learner mixes these up, the result is always wrong by a wide margin. Say it out loud: "base, multiplied by itself, exponent-many times."

## Build It

```python
python phases/00-setup-and-tooling/17-powers-and-exponents/code/powers.py
```

## Why this matters for AI

Everything about model size is powers of two. Bit-widths (16, 8, 4, 2, and the ternary 1.58), the number of values a code can store, memory in bytes, vocabulary sizes, context lengths: all of them are `2^something`. When a paper says "we went from 16 bits to 2 bits", it is saying the storage per weight dropped by a factor of `2^16 / 2^2`. Powers are the native language of hardware.
