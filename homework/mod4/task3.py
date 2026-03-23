def get_nod(a, b):
    if b == 0:
        return a
    else:
        return get_nod(b, a % b)

if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    nod = get_nod(a, b)
    print(nod)