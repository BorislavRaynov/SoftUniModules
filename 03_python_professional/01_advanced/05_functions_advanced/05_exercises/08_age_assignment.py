def age_assignment(*args, **kwargs):
    to_return = ''
    result = {}
    for key, value in kwargs.items():
        for el in args:
            if el.startswith(key):
                result[el] = value
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    for key, value in sorted_result:
        to_return += f"{key} is {value} years old." + '\n'

    return to_return


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
