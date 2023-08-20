import math


def point_location(first, second, third, forth):
    if abs(first) + abs(second) > abs(third) + abs(forth):
        return f"({math.floor(third)}, {math.floor(forth)})({math.floor(first)}, {math.floor(second)})"
    elif abs(first) + abs(second) < abs(third) + abs(forth):
        return f"({math.floor(first)}, {math.floor(second)})({math.floor(third)}, {math.floor(forth)})"
    else:
        return f"({math.floor(first)}, {math.floor(second)})({math.floor(third)}, {math.floor(forth)})"


def line_location(f_st, s_nd, t_rd, f_th, fi_th, s_th, se_th, ei_th):
    if abs(f_st) + abs(s_nd) + abs(t_rd) + abs(f_th) < abs(fi_th) + abs(s_th) + abs(se_th) + abs(ei_th):
        return point_location(fi_th, s_th, se_th, ei_th)
    elif abs(f_st) + abs(s_nd) + abs(t_rd) + abs(f_th) > abs(fi_th) + abs(s_th) + abs(se_th) + abs(ei_th):
        return point_location(f_st, s_nd, t_rd, f_th)
    else:
        return point_location(f_st, s_nd, t_rd, f_th)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
print(line_location(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4))

# f"({math.floor(fi_th)}, {math.floor(s_th)})({math.floor(se_th)}, {math.floor(ei_th)})"