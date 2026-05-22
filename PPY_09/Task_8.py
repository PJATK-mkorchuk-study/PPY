import re


dict = {}

with open("THE HOBBIT.txt", "tr") as file:
    
    words = re.findall("\\w+", file.read())

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1


sorted_words = sorted(dict.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words[:10]:
    print(f"{word}: {count}")
