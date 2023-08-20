def find_result_type(first, second, third):
    lst_nums = [first, second, third]
    if 0 in lst_nums:
        return "zero"
    else:
        count_negative = 0
        for num in lst_nums:
            if num < 0:
                count_negative += 1
        if count_negative % 2 != 0:
            return "negative"
        else:
            return "positive"


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(find_result_type(num_1, num_2, num_3))
