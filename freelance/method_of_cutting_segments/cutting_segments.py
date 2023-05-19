import math

eps = 10 ** (-4)
a = -5
b = 7

a1 = -5
b1 = 0
a2 = 0
b2 = 2
a3 = 2
b3 = 7

fi = (1 + math.sqrt(5)) / 2    # Золотий перетин


def func(x):
    return x ** 3 - 4.1 * x ** 2 + 2.2 * x + 1.4


# Метод дихотомії
def dihotom(a, b):
    ai = a
    bi = b

    while abs(bi - ai) > eps:
        x = (ai + bi) / 2
        if (func(x) * func(ai)) < 0:
            bi = x
        else:
            ai = x

    print(f"Розв'язок рівняння методом дихотомії: {x=}")


dihotom(a1, b1)
dihotom(a2, b2)
dihotom(a3, b3)

print()
# Метод золотого перетину
def golden_section(a, b):
    ai = a
    bi = b

    while abs(bi - ai) > eps:
        x1 = bi - (bi - ai) / fi
        x2 = ai + (bi - ai) / fi
        if abs(func(x1)) > abs(func(x2)):
            ai = x1
        else:
            bi = x2

    x = (ai + bi) / 2
    print(f"Розв'язок рівняння методом золотого перетину: {x=}")


golden_section(a1, b1)
golden_section(a2, b2)
golden_section(a3, b3)

print()

# Метод Фібоначчі

def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_(a, b):
    ai = a
    bi = b
    n = 20

    fi1 = fibonacci(n-2)/fibonacci(n)
    fi2 = fibonacci(n-1)/fibonacci(n)
    x1 = ai + (bi - ai) * fi1
    x2 = ai + (bi - ai) * fi2
    y1 = func(x1)
    y2 = func(x2)

    for _ in range(n):
        if abs(y1) > abs(y2):
            ai = x1
            x1 = x2
            x2 = bi - (x1 - ai)
            y1 = y2
            y2 = func(x2)
        else:
            bi = x2
            x2 = x1
            x1 = ai + (bi - x2)
            y2 = y1
            y1 = func(x1)

    x = (x1 + x2) / 2
    print(f"Розв'язок рівняння методом Фібоначчі: {x=}")


fibonacci_(a1, b1)
fibonacci_(a2, b2)
fibonacci_(a3, b3)

input("Натисніть enter шоб закрити")
