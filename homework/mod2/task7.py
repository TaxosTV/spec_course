string = input()
replacer = string.find(",")
s = string[:replacer]
i = string[replacer + 1]

count = 0
index = 0
while s[index] == i:
    count += 1
    index += 1

print(count)