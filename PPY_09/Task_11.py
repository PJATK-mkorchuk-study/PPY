import re

with open("THE HOBBIT.txt", "tr") as file:
    chapters = re.split("(?m)^Chapter\\b", file.read())
    print(len(chapters) - 1)