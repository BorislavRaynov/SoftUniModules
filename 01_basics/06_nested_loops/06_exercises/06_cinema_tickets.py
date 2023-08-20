movie = input()

count_student = 0
count_standard = 0
count_kid = 0
count_tickets = 0
total_tickets = 0

while movie != "Finish":
    free_seats = int(input())
    type_ticket = input()
    while type_ticket != "End":
        total_tickets += 1
        count_tickets += 1
        if type_ticket == "student":
            count_student += 1
        elif type_ticket == "standard":
            count_standard += 1
        elif type_ticket == "kid":
            count_kid += 1
        if count_tickets >= free_seats:
            break
        type_ticket = input()

    percent_seats = (count_tickets / free_seats) * 100
    print(f"{movie} - {percent_seats:.2f}% full.")
    count_tickets = 0
    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{(count_student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(count_standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(count_kid / total_tickets) * 100:.2f}% kids tickets.")

