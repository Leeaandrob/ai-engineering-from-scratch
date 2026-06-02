# Ratios and Percent

> A percent is just a fraction with the bottom number fixed at 100. "Per cent" literally means "per hundred".

**Type:** Learn
**Languages:** Python
**Prerequisites:** Fractions and Division (00-14)
**Time:** ~30 minutes

## Learning Objectives

- Read a ratio as "this many per that many" and turn it into a single number by dividing
- Convert any fraction to a percent by multiplying the decimal by 100
- Explain what "5 percent" and "97.8 percent recovery" mean in NeuroGrid terms
- Avoid the common direction error (which number goes on the bottom)

## The Concept

You now know that a fraction is a division (lesson 00-14). A **ratio** and a **percent** are both just fractions in disguise.

### A ratio is a comparison by division

A ratio compares two amounts using the word "per": miles per hour, dollars per item, weights per byte. You turn a ratio into one number by dividing:

```
352 km in 5 hours   ->   352 / 5 = 70.4 km per hour
```

The word "per" is your signal to divide. The thing before "per" goes on top, the thing after "per" goes on the bottom.

### A percent is a fraction out of 100

"Per cent" means "per hundred". A percent is a fraction whose bottom is always 100:

```
5%   =   5/100   =   0.05
50%  =  50/100   =   0.5
100% = 100/100   =   1.0
```

To go from a fraction to a percent: do the division to get the decimal, then multiply by 100.

```
17.5 / 352 = 0.0497...   ->   x 100   =   about 5%
```

To go the other way (percent to a plain number): divide by 100. `5% = 5/100 = 0.05`.

### Worked example: accuracy recovery

NeuroGrid's full-precision teacher model scores `0.8474` on a legal task. After squeezing it down to 1.58 bits, the ternary student scores `0.829`. How much of the teacher's quality did we keep? That is a ratio of student over teacher:

```
0.829 / 0.8474 = 0.9783...
```

Multiply by 100: about `97.8%`. We kept 97.8 percent of the quality while cutting the storage to roughly an eighth. The whole pitch of the project lives in that one percentage.

A second example, the size side: a tiny adapter of `17.5` units of something inside a `352`-unit model is:

```
17.5 / 352 = 0.0497   ->   about 5%
```

So the adapter is about 5 percent of the model.

## Active recall

Produce the answer. Easiest first.

1. `50%` as a plain decimal = ?
2. `3/4` as a percent = ?
3. `0.829 / 0.8474` as a percent (round to one decimal) = ?

Answers: `0.5`; `75%` (0.75 x 100); about `97.8%`.

### Misconception callout

The trap is putting the numbers in the wrong order. "Recovery" is student divided by teacher, not teacher divided by student. If you compute `0.8474 / 0.829` you get `1.022`, which would claim the student is *better* than the teacher. Always ask: which is the whole (the bottom) and which is the part (the top)? The part you kept goes on top.

## Build It

```python
python phases/00-setup-and-tooling/15-ratios-and-percent/code/percent.py
```

## Why this matters for AI

Almost every result in this curriculum is reported as a percent or a ratio: accuracy recovery, compression ratio, GPU utilization, tokens per second, fraction of parameters fine-tuned. "We recovered 97.8 percent at one eighth the size" is the kind of sentence that decides whether a model ships. It is one division and one multiply by 100.
