def compare_numbers(numbers:list):
    if numbers.count(numbers[0]) == len(numbers):
        print("Все числа равны")
    elif all([numbers.count(n)==1 for n in set(numbers)]):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

if __name__ == "__main__":
    numbers = list(map(int, input().strip().split(" ")))
    compare_numbers(numbers)