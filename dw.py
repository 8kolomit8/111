A = float(input("Введите число A (> 1): "))
k = 0
sum = 0.0
while sum <= A:
    k += 1
    sum += 1 / k
print(f"Наименьшее целое число K: {k}")
print(f"Сумма 1 + 1/2 + ... + 1/K: {sum:.6f}")
