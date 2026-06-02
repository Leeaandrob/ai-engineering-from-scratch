"""Order of operations: the same numbers, grouped two ways, give two answers."""


def evaluate_chain():
    # multiply before add
    return 2 + 3 * 4  # 14, not 20


def evaluate_grouped():
    # parentheses force the add first
    return (2 + 3) * 4  # 20


def bytes_per_weight(bytes_per_block, weights_per_block):
    # a single division: 34 / 128
    return bytes_per_block / weights_per_block


if __name__ == "__main__":
    print("2 + 3 * 4   =", evaluate_chain())
    print("(2 + 3) * 4 =", evaluate_grouped())
    print("34 / 128    =", bytes_per_weight(34, 128))
    print("34 / (128*2)=", 34 / (128 * 2))
