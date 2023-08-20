def numbers_searching(*args):
    given_nums = list(args)
    duplicates = set()
    result = []

    for num in given_nums:
        if given_nums.count(num) > 1:
            duplicates.add(num)

    for i in range(min(given_nums), max(given_nums) + 1):
        if i not in given_nums:
            result.append(i)

    result.append(sorted(list(duplicates)))

    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
