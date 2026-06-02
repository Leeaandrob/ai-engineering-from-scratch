"""Scientific notation: a number times a power of ten. e means 'times ten to the'."""


def expand(coefficient, exponent):
    # a x 10^b as a plain number
    return coefficient * (10 ** exponent)


def is_smaller(a, b):
    # which learning rate is smaller? compare the actual values
    return a < b


if __name__ == "__main__":
    print("1.75e9 =", expand(1.75, 9))       # 1750000000.0
    print("4.5e-5 =", expand(4.5, -5))       # 4.5e-05
    print("1e-4   =", expand(1, -4))         # 0.0001
    print("4.5e-5 < 1e-4 ?", is_smaller(4.5e-5, 1e-4))  # True
