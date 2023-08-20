def rounding(num):
    result = []
    for number in numbers:
        num = round(float(number))
        result.append(num)
    return result


numbers = input().split()
print(rounding(numbers))
