# Logarithms

> A logarithm is a count. It counts how many times you doubled, starting from 1. That is the whole idea, and it is where the name "1.58-bit" comes from.

**Type:** Learn
**Languages:** Python
**Prerequisites:** Repeated Operations and the Counting Flip (00-16), Powers and Exponents (00-17), Roots and Squares (00-19)
**Time:** ~60 minutes

## Learning Objectives

- Read `log2(x)` as "how many times do I double, starting from 1, to reach x?"
- Compute the integer logs by counting doublings on a ladder
- Explain why `log2(3)` is about `1.585`, the exact number behind "1.58-bit ternary"
- Connect the three views: count the doublings, "2 to the what", and `log2`
- Relate the logarithm to perplexity, `exp(cross-entropy)`

## The Concept

This is the keystone of the whole phase. Take it slowly. We will build the logarithm the way it actually clicks, then connect it to the textbook view at the end.

### A logarithm is a count of doublings

Forget "logarithm" for a second. Go back to the doubling ladder you built in lesson 00-16:

```
start:   1
double:  1 -> 2     (1 doubling)
double:  2 -> 4     (2 doublings)
double:  4 -> 8     (3 doublings)
double:  8 -> 16    (4 doublings)
```

Now the one question that defines this lesson:

> **Starting from 1, how many times do I double to reach this number?**

That count IS the base-2 logarithm. Written `log2`:

```
log2(2)  = 1     (1 -> 2 is one doubling)
log2(4)  = 2     (1 -> 2 -> 4 is two doublings)
log2(8)  = 3     (1 -> 2 -> 4 -> 8 is three doublings)
log2(16) = 4     (four doublings)
```

To find `log2(8)`, you do not compute anything fancy. You walk up the ladder from 1, doubling, and you count your steps until you land on 8. Three steps. `log2(8) = 3`. Done.

### MISCONCEPTION 1 (the most common one)

> **Dividing by 2 once is ONE operation. A logarithm COUNTS how many doublings.**

A learner asked for `log2(8)` will often compute `8 / 2 = 4` and answer 4. That is wrong, and it is worth seeing exactly why. `8 / 2 = 4` undoes a single doubling: it walks you one step DOWN the ladder, from 8 to 4. But the logarithm is not "what is one step down". It is "how many steps total to get back to 1". From 8 you step `8 -> 4 -> 2 -> 1`, which is **three** steps. So `log2(8) = 3`, not 4. One division is a single move; a logarithm is a count of moves. Keep them apart.

### MISCONCEPTION 2 (base versus the count)

> **The base is the thing you double. The logarithm is the count. Do not return the base.**

Asked for `log10(100)`, a learner answered `10`. The 10 is the base (the thing being repeated), not the answer. The question is "how many times do I multiply by 10, starting from 1, to reach 100?":

```
1 -> 10 -> 100     that is TWO steps
```

So `log10(100) = 2`. Not 10, not 100. The answer to a logarithm is always the small counting number, never the base and never the big target.

### MISCONCEPTION 3 (why log2(3) is NOT 1.5)

This is the important one, because it produces the project's signature number.

`3` is not on the doubling ladder. It sits between `2` (one doubling) and `4` (two doublings). So `log2(3)` is between 1 and 2. The tempting guess is the middle, `1.5`, because 3 is the middle of 2 and 4. **That guess is wrong, and here is exactly why.**

The exponent scale does not move by adding, it moves by **multiplying**. The midpoint exponent `1.5` does not land on the arithmetic middle of 2 and 4. From lesson 00-19 you know what `2^1.5` actually is:

```
2^1.5 = 2 x sqrt(2) = 2 x 1.414 = 2.83
```

So the exponent `1.5` lands on `2.83`, not on `3`. To reach `3` you need to go a little PAST 1.5. The true value is:

```
log2(3) = 1.585
```

Check the direction: `2^1.585` is a bit more than `2^1.5 = 2.83`, climbing toward 3. The answer is just past the midpoint, exactly as the multiplying scale predicts. That `1.585` is the "1.58-bit" in NeuroGrid's ternary format.

### The three-views cement

These three sentences all say the exact same thing. When you can flip between them freely, you own the logarithm:

```
count the doublings from 1 to 8   =   "2 to the WHAT gives 8"   =   log2(8)
        3                                      3                          3
```

- **Count the doublings** is how you compute it by hand (this lesson).
- **"2 to the what"** is the inverse-of-an-exponent view (lesson 00-17 ran the exponent forward; the log runs it backward).
- **`log2`** is the symbol you will read in every paper.

Same number, three costumes.

### One honest note about the decimal

You can get the integer answers (`log2(8) = 3`) purely by counting. The DECIMAL part (`log2(3) = 1.585`) needs the fractional exponents and roots from lesson 00-19, which is why that lesson came first. In code you will just call `math.log2`; by hand you can always state the integer bracket ("between 1 and 2, a bit past the middle, so about 1.585").

## Build It

```python
python phases/00-setup-and-tooling/20-logarithms/code/logs.py
```

## Active recall

Produce the answer. Easiest first, so you secure a win before the hard one.

1. `log2(4)` = ? (count the doublings from 1)
2. `log2(8)` = ? (do NOT divide 8 by 2; count the steps)
3. `log10(1000)` = ? (how many times do you multiply by 10 from 1?)
4. Is `log2(3)` closer to 1.5 or to 1.6, and why?

Answers: `2`; `3`; `3`; closer to `1.6` (it is `1.585`), because the exponent `1.5` only reaches `2.83`, so you must go a bit past 1.5 to reach 3.

## Why this matters for AI

Two of the most important numbers in this whole curriculum are logarithms. `log2(3) = 1.585` is the bits-per-weight floor for a ternary value (three options: -1, 0, +1), the exact moat of the project and the source of the "1.58-bit" name. Perplexity, the headline quality number for any language model, is `exp(cross-entropy)`, the inverse log that undoes the natural log hiding inside cross-entropy loss. If logs are fuzzy these are memorized trivia; once logs are a count of doublings, they are obvious.
