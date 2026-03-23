n = int(input())
result = "{} {} {}".format(bin(n)[2:], oct(n)[2:], hex(n)[2:]) if n >= 0 else "Неверный ввод"
print(result)