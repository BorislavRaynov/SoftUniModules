def even_numbers(nums):
    if nums % 2 == 0:
        return True
    else:
        return False


numbers = map(int, (input().split()))
result = filter(even_numbers, numbers)
print(list(result))
