from math import ceil
number_of_people = int(input())
capacity = int(input())
courses = 0
if capacity > 0:
    courses = number_of_people / capacity
print(ceil(courses))
