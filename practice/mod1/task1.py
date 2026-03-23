n = int(input("Введите количество имен N: "))
names = []

for i in range(n):
    name = input(f"Введите имя #{i + 1}: ")
    names.append(name)

uni = []

for name in names:
    if all(len(name) != len(existing_name) for existing_name in uni):
        uni.append(name)

print("Исходный список names:", names)
print("Новый список uni:", uni)