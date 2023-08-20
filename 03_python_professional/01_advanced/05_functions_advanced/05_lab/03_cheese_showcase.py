def sorting_cheeses(**kwargs):
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for key, value in sorted_kwargs:
        sorted_value = sorted(value, reverse=True)
        result += key + '\n'
        result += '\n'.join([str(n) for n in sorted_value]) + '\n'

    return result


kwarg = {'Parmesan': [102, 120, 135], 'Camembert': [100, 100, 105, 500, 430], 'Mozzarella': [50, 125]}
print(sorting_cheeses(**kwarg))
