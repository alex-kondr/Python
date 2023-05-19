def lagrange(x_, y, a):
    ans = 0.0
    for i in range(len(y)):
        t_ = y[i]
        for j in range(len(y)):
            if i != j:
                t_ *= (a - x_[j]) / (x_[i] - x_[j])
        ans += t_
    return ans


x = 6
x_1 = [3, 4, 5, 6, 7]
y_1 = [2, 5, 6, 4, 3]
lagrange = lagrange(x_1, y_1, x)
print(f"Дійсне значення: 4")
print(f"Лагранжева интерполяція: {lagrange}")
input("Натисніть enter шоб закрити")
