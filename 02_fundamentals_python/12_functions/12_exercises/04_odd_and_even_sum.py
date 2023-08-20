def sum_of_even_and_sum_of_odd(number):
    list_of_digits = []
    for i in range(len(number)):
        num = int(number[i])
        list_of_digits.append(num)
    odd_sum = 0
    even_sum = 0
    for element in list_of_digits:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


given_number = input()
print(sum_of_even_and_sum_of_odd(given_number))
