"""A percent is a fraction out of 100. Divide, then multiply by 100."""


def to_percent(part, whole):
    # fraction -> decimal -> percent
    return (part / whole) * 100


def recovery_percent(student, teacher):
    # how much of the teacher's quality the student kept
    return to_percent(student, teacher)


if __name__ == "__main__":
    print("17.5 / 352 =", round(to_percent(17.5, 352), 1), "%")
    print("recovery 0.829 / 0.8474 =", round(recovery_percent(0.829, 0.8474), 1), "%")
    print("3/4 as percent =", to_percent(3, 4), "%")
