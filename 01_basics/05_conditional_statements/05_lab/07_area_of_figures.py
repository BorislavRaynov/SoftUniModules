from math import pi
figure = input()
s = 0
if figure == 'square':
    a = float(input())
    s = a * a
elif figure == 'rectangle':
    b = float(input())
    c = float(input())
    s = b * c
elif figure == 'circle':
    d = float(input())
    s = pi * d ** 2
elif figure == 'triangle':
    e = float(input())
    f = float(input())
    s = e * f / 2
print(f'{s:.3f}')