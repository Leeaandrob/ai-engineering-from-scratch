"""Solve for x by undoing operations, the same on both sides. Rearrange the roofline."""


def solve_linear(a, b, c):
    # solve a*x + b = c for x: undo +b (subtract), then undo *a (divide)
    return (c - b) / a


def tokens_per_second(bandwidth, bytes_per_weight, num_weights):
    return bandwidth / (bytes_per_weight * num_weights)


def bytes_per_weight_for_target(bandwidth, target_tps, num_weights):
    # rearranged roofline: solve the formula above for bytes_per_weight
    return bandwidth / (target_tps * num_weights)


if __name__ == "__main__":
    print("x + 3 = 10 -> x =", solve_linear(1, 3, 10))   # 7
    print("4x = 20    -> x =", solve_linear(4, 0, 20))    # 5
    print("2x + 1 = 9 -> x =", solve_linear(2, 1, 9))     # 4
    tps = tokens_per_second(1000, 2.0, 100)
    print("tps at 2 bytes/weight =", tps)
    print("bytes/weight back-solved =", bytes_per_weight_for_target(1000, tps, 100))
