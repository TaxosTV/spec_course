numbers = input().split(" ")
result = any([numbers.count(n) > 1 for n in set(numbers)])
print(result)