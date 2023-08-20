text = input()

while True:
    try:
        times = int(input())
        print(text * times)
        break
    except ValueError:
        print("Variable times must be an integer")
