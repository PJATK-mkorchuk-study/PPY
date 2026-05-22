import re


with open("THE HOBBIT.txt", "r", encoding="utf-8") as f:
    content = f.read()

parts = re.split(r"(Chapter\b[^\n]*)", content, flags=re.IGNORECASE)

chapters = []

for i in range(1, len(parts) - 1, 2):
    chapters.append((parts[i].strip(), parts[i + 1]))

counts = [(title, body.lower().count("dragon")) for title, body in chapters]
best_title, best_count = max(counts, key=lambda x: x[1])


print(f"\nChapter with most 'dragon' occurrences: {best_title} ({best_count} times)")