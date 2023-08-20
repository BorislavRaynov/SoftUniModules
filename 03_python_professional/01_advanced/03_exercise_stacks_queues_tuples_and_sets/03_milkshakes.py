from collections import deque

milkshakes_count = 0

chocolates = list(map(int, input().split(", ")))
cups_milk = deque(map(int, input().split(", ")))

while milkshakes_count != 5 and (chocolates and cups_milk):
    if chocolates[-1] > 0 and cups_milk[0] > 0:
        if chocolates[-1] == cups_milk[0]:
            milkshakes_count += 1
            chocolates.pop()
            cups_milk.popleft()

        else:
            cups_milk.append(cups_milk.popleft())
            chocolates[-1] -= 5
    else:
        if chocolates[-1] <= 0:
            chocolates.pop()
        if cups_milk[0] <= 0:
            cups_milk.popleft()

    if milkshakes_count == 5:
        made_all_milkshakes = True

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if len(chocolates) <= 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join(list(map(str, chocolates)))}")
if len(cups_milk) <= 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join(list(map(str, cups_milk)))}")
