x = float(input())
y = float(input())
h = float(input())
green_per_l = 3.4
red_per_l = 4.3

s_front = x * x - 1.2 * 2
s_back = x * x
s_left = x * y - 1.5 * 1.5
s_right = s_left
s_green = s_front + s_back + s_left + s_right
total_l_green = s_green / green_per_l

roof_left = x * y
roof_right = x * y
roof_front = x * h / 2
roof_back = roof_front

s_red = roof_back + roof_front + roof_right + roof_left
total_l_red = s_red / red_per_l

print(f'{total_l_green:.2f}')
print(f'{total_l_red:.2f}')
