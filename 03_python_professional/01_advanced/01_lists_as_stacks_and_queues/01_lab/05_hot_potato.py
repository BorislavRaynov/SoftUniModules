from collections import deque
kids = deque(input().split())
tosses = int(input())

tosses_count = 1

while len(kids) > 1:
    if tosses_count != tosses:
        kids.append(kids.popleft())
        tosses_count += 1
    else:
        print(f"Removed {kids.popleft()}")
        tosses_count = 1

print(f"Last is {''.join(kids)}")

