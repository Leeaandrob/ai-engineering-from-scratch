# Scientific Notation

> Very small and very large numbers are painful to write with zeros. Scientific notation writes them as "a number times a power of ten".

**Type:** Learn
**Languages:** Python
**Prerequisites:** Powers and Exponents (00-17)
**Time:** ~30 minutes

## Learning Objectives

- Read and write numbers in the form `a x 10^b` and in `e`-notation (`4.5e-5`)
- Convert between scientific notation and plain decimals
- Compare two magnitudes quickly by looking at the exponent
- Explain why a learning rate of `4.5e-5` is smaller than `1e-4`

## The Concept

Powers of ten are just the doubling ladder from lesson 00-17 but with base 10 instead of 2.

```
10^0 = 1
10^1 = 10
10^2 = 100
10^3 = 1000
```

Each step adds a zero. A positive exponent counts zeros on the right.

### Negative exponents go the other way

A negative exponent means "divide by 10 that many times", which moves the decimal point left:

```
10^-1 = 0.1     (one tenth)
10^-2 = 0.01    (one hundredth)
10^-3 = 0.001   (one thousandth)
```

So `10^-3 = 1 / 10^3 = 1/1000`. Negative exponent = small number; positive exponent = big number.

### The form: a number times a power of ten

Scientific notation writes any number as a small number (usually between 1 and 10) times a power of ten:

```
1750000000  =  1.75 x 10^9     (1.75 billion)
0.000045    =  4.5  x 10^-5
```

The exponent tells you how far and which way the decimal point moved. Positive 9 means "move the point 9 places right". Negative 5 means "move it 5 places left".

### e-notation: how computers write it

Code cannot type a raised exponent, so it uses the letter `e` (for "exponent"):

```
1.75e9   means   1.75 x 10^9   =  1750000000
4.5e-5   means   4.5  x 10^-5  =  0.000045
1e-4     means   1    x 10^-4  =  0.0001
```

Read `e` as "times ten to the". That is all it means.

### Worked example: comparing two learning rates

NeuroGrid's winning quantization-aware training run used a learning rate of `4.5e-5`. An earlier run used `1e-4`. Which is bigger? Comparing zeros is error-prone; comparing exponents is instant.

```
4.5e-5 = 0.000045
1e-4   = 0.0001
```

`1e-4` has exponent -4; `4.5e-5` has exponent -5. The more negative exponent is the smaller number, so `4.5e-5` is smaller than `1e-4` (it is `0.45e-4`, less than half). The winning recipe used a smaller, gentler learning rate. Being able to see that at a glance, from the exponent alone, is the whole point of the notation.

## Active recall

Produce the answer. Easiest first.

1. Write `10^-2` as a plain decimal.
2. Write `2.5e3` as a plain number.
3. Which is bigger, `4.5e-5` or `1e-4`?

Answers: `0.01`; `2500`; `1e-4` is bigger (exponent -4 beats -5).

### Misconception callout

The trap with negative exponents: a more negative exponent is a SMALLER number, not a bigger one. `e-5` is smaller than `e-4`, the same way 0.00001 is smaller than 0.0001. People see the bigger digit "5" and guess `4.5e-5` is larger; it is not, because the -5 drags it down by another factor of ten. Always read the exponent first, the leading digits second.

## Build It

```python
python phases/00-setup-and-tooling/18-scientific-notation/code/scinot.py
```

## Why this matters for AI

Learning rates (`3e-4`, `4.5e-5`), model sizes (`7e9` parameters), loss values (`2.3e-2`), and tolerances (`1e-8`) are all written in this notation, all day, every paper. Picking a learning rate is largely a matter of choosing the right power of ten. If you can compare exponents at a glance, you can read a training config without converting anything in your head.
