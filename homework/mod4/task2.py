def power_recur(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n%2 == 0:
        return power_recur(a*a, n/2)
    else:
        return a * power_recur(a, n-1)


if __name__ == "__main__":
    a, n = map(int, input().split(" "))
    result = power_recur(a, n)
    print(result)