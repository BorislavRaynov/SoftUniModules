def calculation(a, b, operators):
    result = None
    if operators == "multiply":
        result = a * b
    elif operators == "divide":
        result = int(a / b)
    elif operators == "add":
        result = a + b
    elif operators == "subtract":
        result = a - b

    return result


type_operator = input()
first_num = int(input())
second_num = int(input())

print(calculation(first_num, second_num, type_operator))

