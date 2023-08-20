def perfect_number(num):
    sum_of_dividers = 0
    for divider in range(1, num):
        if num % divider == 0:
            sum_of_dividers += divider
    if sum_of_dividers == num:
        print("We have a perfect number!")
        return True
    print("It's not so perfect.")
    return False


given_num = int(input())
perfect_number(given_num)
