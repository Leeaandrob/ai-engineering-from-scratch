"""A logarithm is a count of doublings from 1. log2(3) ~= 1.585 is the '1.58-bit'."""

import math


def log2_by_counting(target):
    # count how many doublings from 1 reach target (integer powers of 2 only)
    # this is NOT target / 2; it is a COUNT of steps
    count = 0
    value = 1
    while value < target:
        value = value * 2
        count = count + 1
    return count


def bits_per_symbol(n):
    # the real-valued log2: bits to encode one of n equally likely symbols
    return math.log2(n)


def perplexity(cross_entropy_nats):
    # exp undoes the natural log inside cross-entropy
    return math.exp(cross_entropy_nats)


if __name__ == "__main__":
    print("log2(8) by counting =", log2_by_counting(8))   # 3, NOT 8/2=4
    print("log2(3) ~=", bits_per_symbol(3))               # ~1.585, the 1.58-bit
    print("2^1.5 =", 2 * math.sqrt(2), "(so 1.5 reaches 2.83, not 3)")
    print("perplexity(ln(50)) =", perplexity(math.log(50)))  # 50
