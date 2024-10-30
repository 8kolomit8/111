M = 80
m1 = 400
g = 9.81
def a1(M, m1, m2):
    return -(m1 - m2) * g / (m1 + m2 + M)
for m2 in range(100, 301, 20):
    a = a1(M, m1, m2)
    print(f"для m2 = {m2}, ускорение a = {a:.2f}")
