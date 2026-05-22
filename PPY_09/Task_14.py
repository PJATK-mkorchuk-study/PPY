import re
from collections import Counter


STOPWORDS = {
    "the", "and", "is", "in", "a", "an", "of", "to", "it", "that", "was",
    "he", "she", "they", "his", "her", "their", "its", "i", "we", "you",
    "me", "my", "your", "our", "this", "with", "for", "on", "at", "by",
    "from", "or", "but", "not", "as", "had", "have", "be", "been", "are",
    "were", "so", "if", "would", "could", "did", "do", "said", "there",
    "then", "when", "what", "which", "who", "all", "one", "out", "up",
    "no", "more", "will", "about", "him", "them", "into", "some", "than",
    "now", "how", "very", "after", "before", "back", "down", "over",
    "just", "off", "also", "any", "other", "time", "well", "got", "still",
    "little", "though", "through", "even", "great", "new", "old", "good",
    "last", "long", "own", "such", "much", "away", "went"
}

with open("THE HOBBIT.txt", "r", encoding="utf-8") as f:
    content = f.read()

words = re.findall(r"[A-Za-z0-9]+", content.lower())
filtered = [w for w in words if w not in STOPWORDS]
frequency = Counter(filtered)

print("10 most frequent words (stopwords removed):")
for word, count in frequency.most_common(10):
    print(f"  {word:<20} {count}")