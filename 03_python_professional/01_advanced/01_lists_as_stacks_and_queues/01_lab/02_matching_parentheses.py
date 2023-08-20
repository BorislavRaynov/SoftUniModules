text = list(input())
index_stack = []
searched_text = ""
for i in range(len(text)):
    if text[i] == "(":
        index_stack.append(i)
    if text[i] == ")":
        for inx in range(index_stack.pop(), i + 1):
            searched_text += text[inx]
        print(searched_text)
        searched_text = ""
