import math

n = int(input("Введите число N: "))

numbers = list(range(n, n ** 2 + 1))
roots = [math.sqrt(x) for x in numbers]

print("Список чисел:", numbers)
print("Список квадратных корней:", roots)