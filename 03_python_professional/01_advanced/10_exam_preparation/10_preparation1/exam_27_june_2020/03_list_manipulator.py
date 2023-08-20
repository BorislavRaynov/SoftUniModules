from collections import deque


def list_manipulator(nums: list, *args):
    numbers = deque(nums)
    command = args[0]
    side = args[1]
    list_last_numbers = list(args[2::])

    if command == "add":
        if side == "beginning":
            numbers.extendleft(reversed(list_last_numbers))

        elif side == "end":
            numbers.extend(list_last_numbers)

    elif command == "remove":

        if side == "beginning":
            if list_last_numbers:
                for i in range(list_last_numbers[0]):
                    numbers.popleft()
            else:
                numbers.popleft()

        elif side == "end":
            if list_last_numbers:
                for i in range(list_last_numbers[0]):
                    numbers.pop()
            else:
                numbers.pop()

    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))

