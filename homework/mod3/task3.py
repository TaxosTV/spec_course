domain = input()
result = domain.split(".")[::-1]
print(*result, sep="\n")