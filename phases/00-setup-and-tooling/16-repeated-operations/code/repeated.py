"""Multiplication is repeated addition. The flip: count how many times you repeat."""


def times_as_repeated_addition(value, count):
    # value x count = value added to itself count times
    total = 0
    for _ in range(count):
        total = total + value
    return total


def double_n_times(n):
    # start at 1, double n times (the operation, forward)
    result = 1
    for _ in range(n):
        result = result * 2
    return result


def count_doublings(target):
    # the counting flip: how many doublings from 1 reach target?
    # step DOWN the ladder and count, do NOT just divide once
    count = 0
    value = 1
    while value < target:
        value = value * 2
        count = count + 1
    return count


if __name__ == "__main__":
    print("3 x 4 as repeated add =", times_as_repeated_addition(3, 4))
    print("double 3 times from 1 =", double_n_times(3))
    print("doublings to reach 8  =", count_doublings(8))
    print("doublings to reach 16 =", count_doublings(16))
