def int_float_str(command, value):
    if command == "int":
        return int(value) * 2
    elif command == "real":
        return f"{float(value) * 1.5:.2f}"
    elif command == "string":
        return f"${value}$"


some_line = input()
other_line = input()
print(int_float_str(some_line, other_line))
