product = input()

type = "unknown"

if product == "banana" or product == "kiwi" or product == "apple" or product == "cherry"\
    or product == "lemon" or product == "grapes":
    type = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    type = "vegetable"
print(type)
