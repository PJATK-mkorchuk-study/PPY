import re

with open("THE HOBBIT.txt", "tr") as file:
    words = re.findall("\\w+", file.read())
    sum = 0
    for word in words:
        sum += len(word)
    print(round(sum / len(words)))
    
    
    