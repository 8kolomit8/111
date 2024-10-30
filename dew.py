def a(c):
    return 1.8 * c + 32
print ("Цельсия (°C) Фаренгейт (°F)")
for c in range(51, 29, -15):
    f = a(c)
    print(f"{c} {f}")
