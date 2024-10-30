def c1(c2):
    return 1.8 * c2 + 32
print("Цельсии (°C) Фаренгейт (°F)")
for c in range(15, 31, 2):
    c2 = c / 2
    f = c1(c2)
    print(f"{c2} {f:.1f}")
