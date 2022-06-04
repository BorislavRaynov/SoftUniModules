number = int(input())
greeting = ""
for i in range(1, number + 1):
    number = int(input())
    if number == 88:
        greeting = "Hello"
    elif number == 86:
        greeting = "How are you?"
    elif number < 88:
        greeting = "GREAT!"
    else:
        greeting = "Bye."
    print(greeting)

