from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0
while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_bee = working_bees.popleft()
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            honey_made = abs(current_bee + current_nectar)
        elif current_symbol == "-":
            honey_made = abs(current_bee - current_nectar)
        elif current_symbol == "*":
            honey_made = abs(current_bee * current_nectar)
        else:
            if current_nectar == 0:
                continue
            honey_made = abs(current_bee / current_nectar)
        total_honey += honey_made


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
