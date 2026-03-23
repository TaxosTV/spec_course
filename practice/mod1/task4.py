phrases = input("Введите фразы через ';': ").split(";")

phrases = [phrase.strip() for phrase in phrases]

lengths = [len(phrase.split()) for phrase in phrases]

print("Исходный список фраз:", phrases)
print("Список lengths:", lengths)