number = int(input())

if number < 0:
    print("Неверный ввод")
    exit(1)

reminder = number

r_2 = ""

while reminder > 0:
    r_2 += str(reminder % 2)
    reminder = reminder // 2

r_8 = ""
reminder = number

while reminder > 0:
    r_8 += str(reminder % 8)
    reminder = reminder // 8


r_16 = ""
reminder = number

while reminder > 0:
    digit = reminder % 16
    if digit == 10: r_16 += "a"
    elif digit == 11: r_16 += "b"
    elif digit == 12: r_16 += "c"
    elif digit == 13: r_16 += "d"
    elif digit == 14: r_16 += "e"
    elif digit == 15: r_16 += "f"
    else:
        r_16 += str(digit)

    reminder = reminder // 16

print(f"{r_2[::-1]}, {r_8[::-1]}, {r_16[::-1]}")