import math

x = int(input("Введите объем шара в куб. ед. (x): "))
r = (3 * x ** 1 / 3) / (4 * math.pi)
print(f"Исковый радиус: {r}")