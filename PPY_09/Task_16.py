import re
 
 
with open("THE HOBBIT.txt", "r", encoding="utf-8") as f:
    content = f.read()
 
words = re.findall(r"[A-Za-z0-9]+", content)
 
print("Concordance for 'Bilbo' (±3 words):\n")
for i, word in enumerate(words):
    if word.lower() == "bilbo":
        start = max(0, i - 3)
        end = min(len(words), i + 4)
        context = words[start:end]
        highlighted = [f"[{w}]" if w.lower() == "bilbo" else w for w in context]
        print("  " + " ".join(highlighted))