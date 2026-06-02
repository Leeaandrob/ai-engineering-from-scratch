"""Three function shapes: linear, exponential, sigmoid. Feed a number, get a number."""

import math


def linear(x):
    # constant change: a straight line
    return 2 * x + 1


def exponential(x):
    # multiplying change: doubles every step
    return 2 ** x


def sigmoid(x):
    # squashes any input into the range 0..1
    return 1 / (1 + math.exp(-x))


if __name__ == "__main__":
    print("linear(4)      =", linear(4))        # 9
    print("exponential(3) =", exponential(3))   # 8
    print("sigmoid(0)     =", sigmoid(0))       # 0.5
    print("sigmoid(-10)   ~=", round(sigmoid(-10), 4))  # ~0
    print("sigmoid(10)    ~=", round(sigmoid(10), 4))   # ~1
