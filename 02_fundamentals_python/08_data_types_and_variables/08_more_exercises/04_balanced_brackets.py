number_lines = int(input())
list_of_str = []
list_of_brackets = []
opened_brackets = 0
closed_brackets = 0
o_brackets = False
c_brackets = False
brackets_are_balanced = False

for i in range(number_lines):
    element = input()
    list_of_str.append(element)

for elements in list_of_str:
    if elements == "(":
        opened_brackets += 1
        list_of_brackets.append(elements)
    elif elements == ")":
        closed_brackets += 1
        list_of_brackets.append(elements)

for i in range(len(list_of_brackets)):
    if i % 2 == 0 and list_of_brackets[i] == "(":
        o_brackets = True
    elif i % 2 == 0 and list_of_brackets[i] != "(":
        o_brackets = False
    if i % 2 != 0 and list_of_brackets[i] == ")":
        c_brackets = True
    elif i % 2 != 0 and list_of_brackets[i] != ")":
        c_brackets = False


if opened_brackets == closed_brackets and o_brackets and c_brackets:
    brackets_are_balanced = True

if brackets_are_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

