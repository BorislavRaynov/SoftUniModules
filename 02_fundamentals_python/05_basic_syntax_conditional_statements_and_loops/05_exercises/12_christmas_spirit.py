decoration_per_shop = int(input())
total_days_left = int(input())

total_cost = 0
total_points = 0

for i in range(1, total_days_left + 1):
    if i % 11 == 0:
        decoration_per_shop += 2
    if i % 2 == 0:
        total_cost += 2 * decoration_per_shop
        total_points += 5
    if i % 3 == 0:
        total_cost += 8 * decoration_per_shop
        total_points += 13
    if i % 5 == 0:
        total_cost += 15 * decoration_per_shop
        total_points += 17
        if i % 5 == 0 and i % 3 == 0:
            total_points += 30
    if i % 10 == 0:
        total_points -= 20
        total_cost += 23

if total_days_left % 10 == 0:
    total_points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_points}")
