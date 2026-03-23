numbers = list(map(int, input("Введите числа через пробел: ").split()))
k = int(input("Введите число K: "))

multiples = [x for x in numbers if x % k == 0]

print("Числа, кратные K:", multiples)