is_exit_loop = False

while (not is_exit_loop):
    a = float(input())

    if (a >= 0):
        print(f"Result: {a * 2:.2f}")
    else:
        print("Negative number!")
        is_exit_loop = True
