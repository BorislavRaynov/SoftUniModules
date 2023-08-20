def get_magic_triangle(num):
    triangle = [[1], [1, 1]]
    for i in range(1, num - 1):
        row = []
        current_len = len(triangle[i])
        for _ in range(current_len + 1):
            if _ == 0:
                row.append(triangle[i][_])
            elif _ == current_len:
                row.append(triangle[i][-1])
            else:
                current_sum = triangle[i][_-1] + triangle[i][_]
                row.append(current_sum)
        triangle.append(row)
    return triangle


print(get_magic_triangle(5))
