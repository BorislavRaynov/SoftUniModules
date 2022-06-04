command = input()
count_coffee = 0
coffee_exceeded = False

while command != "END":
    if command == "cat" or command == "dog" or command == "movie" or command == "coding":
        count_coffee += 1
    elif command == "CAT" or command == "DOG" or command == "MOVIE" or command == "CODING":
        count_coffee += 2
    else:
        command = input()
        continue
    if count_coffee > 5:
        coffee_exceeded = True
        break
    command = input()
if coffee_exceeded:
    print("You need extra sleep")
else:
    print(count_coffee)
