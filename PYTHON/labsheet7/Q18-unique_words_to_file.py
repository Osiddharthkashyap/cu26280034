import re
# Preserve first-seen order while writing unique words to unique_words.txt.
try:
    with open("sample.txt", encoding="utf-8") as file:
        words = re.findall(r"\b[\w']+\b", file.read())
    seen = set()
    unique = []
    for word in words:
        key = word.casefold()
        if key not in seen:
            seen.add(key)
            unique.append(word)
    with open("unique_words.txt", "w", encoding="utf-8") as output:
        output.write("\n".join(unique) + ("\n" if unique else ""))
    print(f"Saved {len(unique)} unique words to unique_words.txt.")
except FileNotFoundError:
    print("sample.txt not found.")
