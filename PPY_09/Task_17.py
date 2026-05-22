import re
from collections import Counter
 
 
with open("THE HOBBIT.txt", "r", encoding="utf-8") as f:
    content = f.read()


sentence_start_positions = set()
sentence_start_positions.add(0)

for m in re.finditer(r"[.!?]\s+", content):
    sentence_start_positions.add(m.end())
 

name_counts = Counter()
for m in re.finditer(r"\b([A-Z][a-z]+)\b", content):
    if m.start() not in sentence_start_positions:
        name_counts[m.group(1)] += 1
 
print("Likely character names (top 20 by frequency):\n")
print(f"  {'Name':<20} {'Count'}")
print(f"  {'-'*20} {'-'*5}")
for name, count in name_counts.most_common(20):
    print(f"  {name:<20} {count}")