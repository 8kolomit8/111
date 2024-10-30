while True:
    while True:
       try: A = float(input('A = '))
       except ValueError:
           print('Введены некорректные данные')
       else: break
    if A <= 1:
        print('Введены некоректные данные')
    else: break
k = 0
sum = 0
while sum <= A:
    k += 1
    sum += 1 / k
print(f"K: {k}")
print(f"сумма: {sum:.6f}")
