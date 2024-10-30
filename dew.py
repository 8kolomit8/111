def c1(c2):
    return 1.8 * c2 + 32
c2=15
print("Цельсии (°C) Фаренгейт (°F)")
while (c2<=30):
    f = c1(c2)
    print(f"{c2} {f:.1f}")
    c2+=1.5

