import re

with open("THE HOBBIT.txt", "tr") as file:
    o = re.split("\\s+", file.read())
    print(len(o) - 1)