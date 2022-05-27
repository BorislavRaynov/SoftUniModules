season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

type_of_sport = 0
price = 0

if season == "Winter":
    if type_of_group == "boys":
        type_of_sport = "Judo"
        price = students_count * 9.60 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "girls":
        type_of_sport = "Gymnastics"
        price = students_count * 9.60 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "mixed":
        type_of_sport = "Ski"
        price = students_count * 10 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95

if season == "Spring":
    if type_of_group == "boys":
        type_of_sport = "Tennis"
        price = students_count * 7.20 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "girls":
        type_of_sport = "Athletics"
        price = students_count * 7.20 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "mixed":
        type_of_sport = "Cycling"
        price = students_count * 9.50 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95

if season == "Summer":
    if type_of_group == "boys":
        type_of_sport = "Football"
        price = students_count * 15 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "girls":
        type_of_sport = "Volleyball"
        price = students_count * 15 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95
    elif type_of_group == "mixed":
        type_of_sport = "Swimming"
        price = students_count * 20 * nights_count
        if students_count >= 50:
            price = price * 0.50
        elif 20 <= students_count < 50:
            price = price * 0.85
        elif 10 <= students_count < 20:
            price = price * 0.95

print(f"{type_of_sport} {price:.2f} lv.")