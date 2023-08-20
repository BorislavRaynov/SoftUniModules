def start_spring(**kwargs):
    result = ''
    objects = {}
    for key, value in kwargs.items():
        if value not in objects:
            objects[value] = []
        objects[value].append(key)
    for val in objects.values():
        val.sort()
    sorted_objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for v, k in sorted_objects:
        result += f"{v}:\n"
        for el in k:
            result += f"-{el}\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

