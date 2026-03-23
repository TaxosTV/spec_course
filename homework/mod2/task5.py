domain = input()

index = domain.find(".")
result = ""

while index > 0:
    level = domain[:index]
    result = level + "\n" + result
    domain = domain[index + 1:]
    index = domain.find(".")

result = domain + "\n" + result
print(result)