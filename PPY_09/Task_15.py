import re
from collections import Counter
 
 
with open("THE HOBBIT.txt", "r", encoding="utf-8") as f:
    content = f.read()
 
total_lines = len(content.splitlines())
words = re.findall(r"[A-Za-z0-9]+", content)
total_words = len(words)
frequency = Counter(w.lower() for w in words)
top5 = frequency.most_common(5)
 
with open("hobbit_summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Total words : {total_words}\n")
    f.write(f"Total lines : {total_lines}\n")
    f.write("5 most common words:\n")
    for word, count in top5:
        f.write(f"  {word}: {count}\n")
 
print(f"Summary written to {"hobbit_summary.txt"}")
print(f"  Total words : {total_words}")
print(f"  Total lines : {total_lines}")
print("  5 most common words:")
for word, count in top5:
    print(f"    {word}: {count}")