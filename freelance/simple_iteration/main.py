def func(x1, x2, x3, x4):
    x1_next = 42/5 - (1/5) * x2 + (1/5) * x3 - (1/5) * x4
    x2_next = -2 + (1/4) * x1 + (1/4) * x3 - (1/4) * x4
    x3_next = 1/4 + (1/4) * x1 - (1/4) * x2 - (1/4) * x4
    x4_next = -(16/5) + (1/5) * x1 + (2/5) * x2 + (1/5) * x3
    return x1_next, x2_next, x3_next, x4_next


def deviation(x: tuple, x_next: tuple):
    difference = []
    for xi, x_nexti in zip(x, x_next):
        difference.append(abs(xi-x_nexti))
    return max(difference)



def iteration(x, count_iteration):
    count = 0
    local_x = x
    for _ in range(count_iteration):
        x_start = local_x
        local_x = func(*x_start)
        error = deviation(x_start, local_x)
        count += 1

        if round(error*10**6) > 17 and round(error*10**6) < 50:
            break

    print("\nЗначення xi:\n")

    for i, xi in enumerate(local_x):
        print(f"x{i+1} = {round(xi, 2)}")

    print(f"\nТовщина плівки = {round(error*10**6)} мкм\n")
    print(f"Кількість ітерацій: {count}")


x = []

print("Введіть початкові значення xi:")

for i in range(1, 5):
    xi = float(input(f"x{i}: "))
    x.append(xi)


iteration(x, 100)

input("Натисніть enter шоб закрити")








