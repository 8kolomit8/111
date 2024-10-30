A = float(input("Введите число A (> 1): "))
k = 0
sum = 0.0
while sum <= A:
    k += 1
    sum += 1 / k
print(f"K: {k}")
print(f"сумма: {sum:.6f}")
