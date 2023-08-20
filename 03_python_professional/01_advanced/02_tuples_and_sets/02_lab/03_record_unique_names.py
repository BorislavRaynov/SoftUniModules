count_people = int(input())
correct_people = set()

for people in range(count_people):
    correct_people.add(input())

for person in correct_people:
    print(person)
