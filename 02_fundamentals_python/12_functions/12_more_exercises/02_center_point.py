import math


def point_location(first, second, third, forth):
    if abs(first) + abs(second) > abs(third) + abs(forth):
        return f"({math.floor(third)}, {math.floor(forth)})"
    elif abs(first) + abs(second) < abs(third) + abs(forth):
        return f"({math.floor(first)}, {math.floor(second)})"
    else:
        return f"({math.floor(first)}, {math.floor(second)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(point_location(x_1, y_1, x_2, y_2))
