from collections import deque
people = deque()
current_name = input()

while current_name != "End":
    if current_name == "Paid":
        while len(people) > 0:
            print(people.popleft())
    else:
        people.append(current_name)
    current_name = input()

print(f"{len(people)} people remaining.")
