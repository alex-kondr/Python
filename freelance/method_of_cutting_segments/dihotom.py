eps = 10**(-4)
a = -5
b = 7

a1 = -5
b1 = 0
a2 = 0
b2 = 2
a3 = 2
b3 = 7


def func(x):
    return x**3 - 4.1 * x**2 + 2.2 * x + 1.4

def iteration(a, b):
    ai = a
    bi = b

    while abs(bi - ai) > eps:
        x = (ai + bi)/2
        # x = func(x)

        if (func(x) * func(ai)) < 0:
            bi = x
        else:
            ai = x

    print(f"{ai=}")
    print(f"{bi=}")
    print(f"{x=}")
    print(f"eps = {bi-ai}\n\n")


iteration(a1, b1)
iteration(a2, b2)
iteration(a3, b3)
