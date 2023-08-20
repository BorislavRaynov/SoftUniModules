from collections import deque

quantity_for_day = int(input())
orders_quantity = deque(map(int, input().split()))
print(max(orders_quantity))
food_has_finished = False

for order in range(len(orders_quantity)):
    if quantity_for_day >= orders_quantity[0]:
        quantity_for_day -= orders_quantity[0]
        orders_quantity.popleft()
    else:
        food_has_finished = True
        break

if food_has_finished:
    print(f"Orders left: {' '.join(map(str, orders_quantity))}")
else:
    print("Orders complete")
