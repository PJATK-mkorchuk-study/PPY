import re
count = 1
with open("THE HOBBIT.txt", "tr") as file:
    chapters = re.split("(?m)^Chapter\\b", file.read())
    
    for chapter in chapters:
        words = re.findall("\\bBilbo\\b", chapter)
        print(f"Count in chapter {count}: {len(words)}")
        count+=1