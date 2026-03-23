input_string =  input() # 332, 13

index = input_string.find(", ")
first_number = int(input_string[:index])
second_number = int(input_string[index+2:])
reminder = first_number % second_number

print(reminder)

