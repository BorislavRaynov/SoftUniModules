animal_name = input()

if animal_name == "dog":
    print("mammal")
elif animal_name == "crocodile" or animal_name == "tortoise" or animal_name == "snake":
    print("reptile")
else:
    print("unknown")