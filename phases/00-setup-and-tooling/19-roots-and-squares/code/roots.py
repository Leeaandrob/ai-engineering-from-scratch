"""A root is the inverse of a power. sqrt(2) ~= 1.414; 2^1.5 = 2 x sqrt(2) ~= 2.83."""

import math


def square_root(x):
    # the inverse of squaring: what number times itself gives x
    return math.sqrt(x)


def vector_length(a, b):
    # sqrt of the sum of squares (Pythagoras)
    return math.sqrt(a * a + b * b)


def two_to_the_1_5():
    # 2^1.5 = 2 x sqrt(2), the number the log lesson needs
    return 2 * math.sqrt(2)


if __name__ == "__main__":
    print("sqrt(2)  =", square_root(2))          # ~1.414
    print("sqrt(13) =", vector_length(3, 2))     # ~3.606
    print("sqrt(25) =", vector_length(3, 4))     # 5.0
    print("2^1.5    =", two_to_the_1_5())        # ~2.83
