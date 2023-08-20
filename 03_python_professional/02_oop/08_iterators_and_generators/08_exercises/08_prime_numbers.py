def get_primes(nums: list):
    filtered_nums = [n for n in nums if n > 0]

    for n in filtered_nums:
        decimal = 0
        for dec in range(1, n + 1):
            if n % dec == 0:
                decimal += 1
        if decimal == 2:
            yield n


print(list(get_primes([-2, 0, 0, 1, 1, 0])))