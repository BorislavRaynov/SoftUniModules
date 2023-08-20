def tribonacci_sec(number):
    result = [1, 1, 2]
    start = 0
    end = 3
    if number < 3:
        lst_result = []
        for i in range(number):
            lst_result.append(result[i])
        return " ".join(list(map(str, lst_result)))
    else:
        while len(result) != number:
            num_to_be_added = 0
            for index in range(start, end):
                num_to_be_added += result[index]
            result.append(num_to_be_added)
            start += 1
            end += 1
        return " ".join(list(map(str, result)))


num = int(input())
print(tribonacci_sec(num))
