def a(c):
    return 1.8 * c + 32
print(f"{'Celsius (°C)':<15} {'Fahrenheit (°F)':<15}")
for c in range(51, 29, -15):
    f = a(c)
    print(f"{c:<15} {f:<15.2f}")
