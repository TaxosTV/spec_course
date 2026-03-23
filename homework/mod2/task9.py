phone_number = input()

replaces = '-)( '
for replacer in replaces:
    index = phone_number.find(replacer)
    while index > 0:
        phone_number = phone_number[0:index] + phone_number[index+1:]
        index = phone_number.find(replacer)

print(phone_number)