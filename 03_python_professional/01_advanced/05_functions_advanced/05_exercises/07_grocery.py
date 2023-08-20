def grocery_store(**kwargs):
    result = ''
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for key, value in sorted_kwargs:
        result += f"{key}: {value}" + '\n'

    return result


print(grocery_store(bread=5, pasta=12, eggs=12,))
