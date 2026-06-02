# Fractions and Division

> A fraction is not a new thing. A fraction IS a division, written with the divide sign turned sideways.

**Type:** Learn
**Languages:** Python
**Prerequisites:** The Four Operations and Order (00-13)
**Time:** ~30 minutes

## Learning Objectives

- See that the fraction a/b is exactly the division a divided by b
- Convert a fraction into a decimal by doing the division
- Read a decimal as "how much of one whole"
- Compute 34/128 and explain what 0.266 bytes per weight means

## The Concept

You already know division from lesson 00-13. A fraction is the same operation wearing a different costume.

```
3/4   means   3 divided by 4
```

The line in the middle is a division sign. The top number (numerator) is what gets divided. The bottom number (denominator) is what you divide by. That is the entire definition. There is nothing else to a fraction.

### A fraction is a division you have not done yet

`3/4` is a paused division. You can leave it paused (useful when you want an exact value) or you can press play and get a decimal:

```
3 / 4 = 0.75
```

Both are the same quantity. `3/4` and `0.75` are two spellings of "three quarters of one whole".

### Reading a decimal

A decimal answers "how much of one whole do I have?".

- `0.75` is most of a whole (three quarters).
- `0.5` is exactly half.
- `0.266` is about a quarter, a bit more.
- `1.75` is one whole plus three quarters.

The digits after the dot are pieces of one. The first place is tenths (1/10), the next is hundredths (1/100), and so on. So `0.75` is 7 tenths plus 5 hundredths.

### Why dividing by a bigger bottom makes a smaller number

If you share 3 cookies among 4 people, each gets less than one cookie (0.75). Share the same 3 cookies among 100 people and each gets almost nothing (0.03). Bigger denominator, smaller share. This intuition matters in the next lesson on ratios.

### Worked example: bytes per weight

NeuroGrid packs 128 ternary weights into a block that costs 34 bytes of storage. How many bytes does one weight cost on average? That is a fraction, which is a division:

```
34 / 128 = 0.265625
```

So each ternary weight costs about `0.266` bytes. Compare that to a normal 16-bit weight, which costs `2` bytes (16 bits / 8 bits-per-byte). The ternary weight is roughly `0.266 / 2`, about one eighth, of the storage. That single fraction is why the model fits where others do not.

## Active recall

Produce the decimal yourself. Easiest first.

1. `1/2` as a decimal = ?
2. `1/4` as a decimal = ?
3. `34/128` as a decimal = ? (do the division)

Answers: `0.5`; `0.25`; `0.265625` (about 0.266).

### Misconception callout

The trap is thinking a fraction is a "pair of numbers" rather than one number. `3/4` is a single value, `0.75`. Whenever a fraction looks confusing, do the division and read the decimal. The fraction and the decimal are never two different amounts.

## Build It

```python
python phases/00-setup-and-tooling/14-fractions-and-division/code/fractions.py
```

## Why this matters for AI

Bytes per weight, compression ratio, fraction of parameters trained, fraction of accuracy recovered: these are all fractions, which are all divisions. The headline "1.58 bits" and "0.266 bytes" numbers are fractions you can now compute by hand. Decimals are how every one of these gets reported.
