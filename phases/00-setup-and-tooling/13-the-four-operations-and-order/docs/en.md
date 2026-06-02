# The Four Operations and Order

> When a line of math mixes plus and times, the answer depends on what you do first. There is one agreed order.

**Type:** Learn
**Languages:** Python
**Prerequisites:** None beyond the four operations: addition, subtraction, multiplication, division
**Time:** ~30 minutes

## Learning Objectives

- Read a math expression that mixes the four operations and evaluate it in the correct order
- State the order of operations (parentheses, then multiply/divide, then add/subtract)
- Explain why grouping with parentheses changes the answer
- Trace the evaluation order inside the expression 34 / 128

## The Concept

You already know the four operations: addition (+), subtraction (-), multiplication (x), and division (/). That is the whole floor we build on. Everything in this phase is a small twist on these four.

The first twist is tiny but it trips up almost everyone. When a single line mixes operations, the answer is not "left to right". Look:

```
2 + 3 x 4
```

If you go left to right you get `2 + 3 = 5`, then `5 x 4 = 20`. Wrong. The agreed answer is `14`. Why? Because multiplication is done before addition. You compute `3 x 4 = 12` first, then `2 + 12 = 14`.

This is not a rule someone invented to be annoying. Multiplication is repeated addition (the next lesson builds this), so `3 x 4` is a single bundled quantity, `12`, that was already "packed up" before the `+` ever runs.

### The order

Do the operations in this order, top to bottom:

1. **Parentheses** first. Anything inside `( )` is computed before it touches the outside.
2. **Multiply and divide** next, left to right among themselves.
3. **Add and subtract** last, left to right among themselves.

A common name for this is PEMDAS (Parentheses, Exponents, Multiply, Divide, Add, Subtract). Exponents come in lesson 00-17; ignore the E for now.

### Parentheses override the order

Parentheses are a manual override. They say "do this part first, no matter what".

```
2 + 3 x 4   = 2 + 12 = 14
(2 + 3) x 4 = 5 x 4   = 20
```

Same numbers, same operations, different grouping, different answer. The parentheses force the addition to happen before the multiplication.

### Worked example: the order inside 34 / 128

In NeuroGrid, a block of 128 ternary weights is stored using 34 bytes (you will see exactly where these numbers come from later). The "bytes per weight" is:

```
34 / 128
```

That is a single division, so there is no ordering puzzle yet. But suppose you wanted "bytes per weight, then doubled for a safety copy":

```
34 / 128 x 2
```

Division and multiplication share the same level, so go left to right: `34 / 128 = 0.265625` first, then `x 2 = 0.53125`. If instead you meant "34 divided by the quantity 128 times 2", you must write the parentheses:

```
34 / (128 x 2) = 34 / 256 = 0.1328125
```

The parentheses are the difference between a right answer and a wrong one. Engineers write them generously.

## Active recall

Produce the answer yourself before reading on. Easiest first.

1. `10 - 2 x 3` = ?
2. `(10 - 2) x 3` = ?
3. `20 / 4 / 5` = ? (remember: left to right among divisions)

Answers: `4`; `24`; `1` (20/4 = 5, then 5/5 = 1).

### Misconception callout

The trap is "always go left to right". You go left to right only **within the same level**. Multiply/divide as a group beats add/subtract as a group. When unsure, add parentheses to make your intent explicit. The computer will never guess what you meant.

## Build It

```python
python phases/00-setup-and-tooling/13-the-four-operations-and-order/code/order.py
```

## Why this matters for AI

Every formula later in this phase and the next is a line that mixes operations. The roofline throughput, the bytes-per-weight, the learning-rate schedule, the dot product: each is an expression where one wrong grouping gives a number that is off by a factor of hundreds. Getting the order right is the difference between a model that runs and a number you cannot trust.
