string = input()

length = len(string)
index = 0
sum_of_one = 0
while index < length:
    sum_of_one += int(string[index])
    index += 1

sum_of_zeros = length - sum_of_one
if sum_of_zeros == sum_of_one:
    print("yes")
else:
    print("no")