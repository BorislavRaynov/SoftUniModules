rows = int(input())

matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split())))

while True:
    command = input()
    if command == "END":
        for element in matrix:
            print(" ".join(list(map(str, element))))
        break
    com = command.split()
    current_command = com[0]
    rol, col, value = int(com[1]), int(com[2]), int(com[3])
    if rol in range(0, len(matrix)) and col in range(0, len(matrix)):
        if current_command == "Add":
            matrix[rol][col] += value
        elif current_command == "Subtract":
            matrix[rol][col] -= value
        continue
    print("Invalid coordinates")
