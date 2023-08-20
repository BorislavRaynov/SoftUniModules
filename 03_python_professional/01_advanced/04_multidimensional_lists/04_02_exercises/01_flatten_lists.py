string = input().split("|")

matrix = reversed(string)
new_matrix = []
for element in matrix:
    new_element = element.split()
    new_matrix.extend(new_element)

print(' '.join(new_matrix))
