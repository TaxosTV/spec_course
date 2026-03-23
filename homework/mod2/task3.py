input_string = input()

index_first_space = input_string.find(" ")

first_number = int(input_string[:index_first_space])

input_string = input_string[index_first_space+1:]
index_second_space = input_string.find(" ")

second_number = int(input_string[:index_second_space])
third_number = int(input_string[index_second_space+1:])

if first_number < second_number:
    min = first_number
    middle = second_number
elif second_number < first_number:
    min = second_number
    middle = first_number

if middle < third_number:
    result = middle
elif (third_number < middle) and (third_number > min):
    result = third_number
elif third_number < min:
    result = min

print(f"{result}")