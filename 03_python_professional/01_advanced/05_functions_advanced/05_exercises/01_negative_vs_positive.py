def sum_numbers(*args):
    result = 0
    for el in args:
        result += el
    return result


def compare_nums(pos, neg):
    if abs(pos) > abs(neg):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]
positive_n = [x for x in numbers if x > 0]
negative_n = [x for x in numbers if x < 0]

print(sum_numbers(*negative_n))
print(sum_numbers(*positive_n))
print(compare_nums(sum_numbers(*positive_n), sum_numbers(*negative_n)))
