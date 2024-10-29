# Ввод числа A
A = float(input("Введите число A (> 1): "))

# Начальные значения
k = 0
sum_series = 0.0

# Цикл для нахождения K и суммы
while sum_series <= A:
    k += 1
    sum_series += 1 / k

# Вывод результата
print(f"Наименьшее целое число K: {k}")
print(f"Сумма 1 + 1/2 + ... + 1/K: {sum_series:.6f}")
