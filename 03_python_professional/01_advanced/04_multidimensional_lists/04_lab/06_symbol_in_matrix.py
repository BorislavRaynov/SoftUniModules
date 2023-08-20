size = int(input())
matrix = []
for _ in range(size):
    matrix.append([n for n in input()])
searched_symbol = input()
searched_symbol_is_found = False
for r in range(size):
    for c in range(size):
        if matrix[r][c] == searched_symbol:
            result = (r, c)
            searched_symbol_is_found = True
            print(result)
            break
    if searched_symbol_is_found:
        break
if not searched_symbol_is_found:
    print(f"{searched_symbol} does not occur in the matrix")
