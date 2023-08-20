import os
# Нужно е да се въведе "./Files" като инпут за да се работи само с дадените по условие файлове.
directory = input()
result = []
extensions = {}

for root, d_names, f_names in os.walk(directory):
    for name in f_names:
        key = name.split(".")[1]
        if key not in extensions:
            extensions[key] = []
        extensions[key].append(name)

extensions = sorted(extensions.items(), key=lambda x: (x[0], x[1]))

with open(f"{directory}/report.txt", "w") as output_file:
    for key, value in extensions:
        output_file.write(f".{key}\n")
        for v in value:
            output_file.write(f"- - - {v}\n")
