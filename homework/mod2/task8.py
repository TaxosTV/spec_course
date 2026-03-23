string = input()

replacer = string.find(" ")
result = ""
while replacer > 0:
    word = string[:replacer]
    result += word[-1]
    string = string[replacer+1:]
    replacer = string.find(" ")

result += string[-1]
print(result)