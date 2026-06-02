"""A fraction is a division. Do the division to get the decimal."""


def fraction_to_decimal(numerator, denominator):
    # the fraction a/b IS the division a / b
    return numerator / denominator


def bytes_per_weight():
    # 128 ternary weights packed into 34 bytes
    return fraction_to_decimal(34, 128)  # ~0.266


if __name__ == "__main__":
    print("3/4   =", fraction_to_decimal(3, 4))
    print("1/2   =", fraction_to_decimal(1, 2))
    print("34/128 =", bytes_per_weight())
    print("fp16 weight costs 16/8 =", fraction_to_decimal(16, 8), "bytes")
