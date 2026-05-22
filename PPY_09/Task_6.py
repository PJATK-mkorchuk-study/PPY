import re

with open("THE HOBBIT.txt", "tr") as file:
    words = re.findall("\\w+", file.read())

    longest_word = max(words, key=len)
    print(longest_word)