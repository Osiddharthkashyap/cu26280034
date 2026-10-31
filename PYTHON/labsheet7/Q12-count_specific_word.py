import re
# Count whole-word occurrences, ignoring case.
try:
    word = input("Word to count: ").strip()
    if not word:
        raise ValueError("Word cannot be empty.")
    with open("sample.txt", encoding="utf-8") as file:
        text = file.read()
    count = len(re.findall(rf"\b{re.escape(word)}\b", text, re.IGNORECASE))
    print(f"'{word}' occurs {count} time(s).")
except FileNotFoundError:
    print("sample.txt not found.")
except ValueError as error:
    print(error)
