side_length = int(input())

perimetr = 4 * side_length
area = side_length ** 2
diagonal = round(pow(2 * side_length ** 2, 0.5), 2)

print(f"{perimetr:.2f}, {area:.2f}, {diagonal:.2f}")
