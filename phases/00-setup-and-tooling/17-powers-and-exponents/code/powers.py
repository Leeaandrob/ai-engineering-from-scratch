"""An exponent is repeated multiplication. The base, multiplied by itself, exponent-many times."""


def power(base, exponent):
    # base multiplied by itself, exponent times
    result = 1
    for _ in range(exponent):
        result = result * base
    return result


def values_in_bits(num_bits):
    # how many distinct values a code of num_bits can store: 2^num_bits
    return power(2, num_bits)


if __name__ == "__main__":
    print("2^3  =", power(2, 3))
    print("2^10 =", power(2, 10))   # 1024
    print("2^0  =", power(2, 0))    # 1
    print("2-bit code values =", values_in_bits(2))   # 4
    print("1 byte (8 bits) values =", values_in_bits(8))  # 256
