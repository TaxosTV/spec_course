words = input().split(" ")
result = "".join([w[-1] for w in words])
print(result)