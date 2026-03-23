prices = list(map(int, input("Введите цены на товары через пробел: ").split()))
k = int(input("Введите число K: "))
m = int(input("Введите число M: "))

# каждые полные K рублей дают скидку M рублей
discount = [price - (price // k) * m for price in prices]

print("Цены до скидки:", prices)
print("Цены после скидки:", discount)