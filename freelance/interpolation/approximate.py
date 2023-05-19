x = [3, 4, 5, 6, 7]
y = [2, 5, 6, 4, 3]
n = 5

b00 = n
b01 = sum(x)
b10 = b01
b02 = sum([xi**2 for xi in x])
b11 = b02
b20 = b02
b21 = sum([xi**3 for xi in x])
b12 = b21
b22 = sum([xi**4 for xi in x])
c0 = sum(y)
c1 = sum([xi*yi for xi, yi in zip(x, y)])
c2 = sum([xi*yi**2 for xi, yi in zip(x, y)])


def func_first(x):
    return 3.5 + 0.1 * x


def func_second(x):
    return -159.11 + 69.7 * x - 7.07 * x**2


if __name__ == "__main__":
    y_first_order = [func_first(xi) for xi in x]
    error_first_order = round(sum([(yi-yif)**2 for yi, yif in zip(y, y_first_order)]), 2)
    y_second_order = [round(func_second(xi), 2) for xi in x]
    error_second_order = round(sum([(yi-yif)**2 for yi, yif in zip(y, y_second_order)]), 2)
    print(f"{y=}")
    print(f"{y_first_order=}")
    print(f"{error_first_order=}")
    print(f"{y_second_order=}")
    print(f"{error_second_order=}")

