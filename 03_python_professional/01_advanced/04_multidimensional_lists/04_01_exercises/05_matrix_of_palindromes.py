rows, cols = map(int, input().split())
matrix = []
sub_matrix = []
first_letter = chr(97)
last_letter = first_letter

for r in range(rows):
    sub_matrix = []
    for c in range(cols):
        mid_letter = r + c
        sub_matrix.append(chr(ord(first_letter) + r) + chr(ord(first_letter) + mid_letter) + chr(ord(last_letter) + r))
    matrix.append(sub_matrix)

for el in matrix:
    print(" ".join(el))

