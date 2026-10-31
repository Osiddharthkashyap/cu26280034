# Search for a whole word, ignoring letter case.
import re
try:
    word = input("Word to search: ").strip()
    if not word:
        raise ValueError("Search word cannot be empty.")
    text = open("sample.txt", encoding="utf-8").read()
    matches = list(re.finditer(rf"\b{re.escape(word)}\b", text, re.IGNORECASE))
    if matches:
        print(f"'{word}' found {len(matches)} time(s).")
    else:
        print(f"'{word}' was not found.")
except FileNotFoundError:
    print("sample.txt not found.")
except ValueError as error:
    print(error)
