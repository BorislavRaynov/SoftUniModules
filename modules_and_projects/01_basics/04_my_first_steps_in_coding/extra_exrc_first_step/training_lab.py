w = float(input())
h = float(input())

free_width_sm = h * 100 - 100
count_in_free_width = free_width_sm // 70
free_lenght_sm = w * 100
count_in_free_lenght = free_lenght_sm // 120

total_count = count_in_free_width * count_in_free_lenght - 3
print(total_count)