from collections import deque

males = deque(x for x in map(int, input().split()) if x > 0)
females = deque(x for x in map(int, input().split()) if x > 0)
total_matches = 0

while males and females:
    male = males[-1]
    female = females[0]
    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.popleft()
        continue
    elif male % 25 == 0:
        males.pop()
        males.pop()
    elif female % 25 <= 0:
        females.popleft()
        females.popleft()
    else:
        if male == female:
            total_matches += 1
            males.pop()
            females.popleft()
        else:
            males[-1] -= 2
            females.popleft()

print(f"Matches: {total_matches}")
if males:
    males.reverse()
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
