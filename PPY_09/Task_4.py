import re

with open("THE HOBBIT.txt", "tr") as file:
    words = re.findall("\\bBilbo\\b", file.read())
    print(len(words))