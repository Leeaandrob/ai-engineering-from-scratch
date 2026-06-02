"""Summation is a loop that adds up a list. The dot product is a sum of products."""


def sum_to_n(n):
    # sum from i=1 to n of i
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


def sum_of_squares(n):
    # sum from i=1 to n of i^2
    total = 0
    for i in range(1, n + 1):
        total = total + i * i
    return total


def dot_product(a, b):
    # sum of (a[i] x b[i]): the first formula of Phase 1
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


if __name__ == "__main__":
    print("sum 1..4        =", sum_to_n(4))          # 10
    print("sum of squares  =", sum_of_squares(3))    # 14
    print("dot product     =", dot_product([1, 2, 3], [4, 5, 6]))  # 32
