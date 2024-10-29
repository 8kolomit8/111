# Функция для перевода температуры из Цельсия в Фаренгейт
def celsius_to_fahrenheit(celsius):
    return 1.8 * celsius + 32

# Заголовок таблицы
print(f"{'Celsius (°C)':<15} {'Fahrenheit (°F)':<15}")

# Цикл для создания таблицы
for celsius in range(51, 29, -15):  # от 51 до 30 с шагом -15
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:<15} {fahrenheit:<15.2f}")
