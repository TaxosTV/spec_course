def get_palindrome(word):

    letters = set(word)
    count_letters = {l: word.count(l) for l in letters}
    odds = list(filter(lambda c: c[1] % 2 != 0, count_letters.items()))

    middle = ""
    if len(odds) > 1:
        return "Нельзя составить полиндром"

    elif len(odds) == 1:
        middle = odds[0][0]
        count_letters[middle] -= 1
        if count_letters[middle] == 0:
            count_letters.pop(middle)

    half_counts = {k: int(v/2) for k, v in count_letters.items()}

    left_polyndrome = ""
    not_all_elem = True

    while not_all_elem:
        for item in half_counts.items():
            if item[1] == 0:
                continue
            letter = item[0]
            left_polyndrome += letter
            half_counts[letter] -= 1
        if all(map(lambda i: i[1] == 0, half_counts.items())):
            not_all_elem = False

    return left_polyndrome + middle + left_polyndrome[::-1]


if __name__ == "__main__":
    word = input()
    print(get_palindrome(word))