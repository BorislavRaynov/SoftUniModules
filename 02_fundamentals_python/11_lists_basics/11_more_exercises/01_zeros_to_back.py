numbers = input().split(", ")

for i in range(len(numbers)):
    if numbers[i] == "0":
        numbers.append(numbers.pop(numbers.index("0")))
numbers = list(map(int, numbers))
print(numbers)
