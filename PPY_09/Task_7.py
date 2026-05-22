import re

with open("THE HOBBIT.txt", "tr") as file:
    words = re.findall("\\w+", file.read())
    unique_words = set(words)
    print(len(unique_words))