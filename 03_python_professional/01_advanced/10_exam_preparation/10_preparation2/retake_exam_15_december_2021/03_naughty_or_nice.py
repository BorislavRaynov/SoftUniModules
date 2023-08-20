def naughty_or_nice_list(*args, **kwargs):
    result = ''
    final_result = {"Nice": [], "Naughty": [], "Not found": []}
    kids_values = {}
    lst_kids = args[0]
    commands = list(args[1::])

    for el in lst_kids:
        if int(el[0]) not in kids_values:
            kids_values[int(el[0])] = []
        kids_values[int(el[0])].append(el[1])

    for com in commands:
        com = com.split('-')
        counting_number = int(com[0])
        current_condition = com[1]
        if counting_number in kids_values:
            if len(kids_values[counting_number]) == 1:
                final_result[current_condition].extend(kids_values[counting_number])
                kids_values.pop(counting_number)

    for string, value in kwargs.items():
        count_name = 0
        for v in kids_values.values():
            count_name += v.count(string)
        if count_name == 1:
            final_result[value].append(string)
            for k, name in kids_values.items():
                for n in name:
                    if n == string:
                        name.remove(n)

    for key, val in kids_values.items():
        if val:
            final_result["Not found"].extend(val)

    for c, v in final_result.items():
        if v:
            result += f"{c}: {', '.join(v)}\n"

    return result


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

