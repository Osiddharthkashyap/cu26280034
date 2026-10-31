import re
# Sort words alphabetically without changing the original file.
try:
    with open("sample.txt", encoding="utf-8") as file:
        words = re.findall(r"\b[\w']+\b", file.read())
    words.sort(key=str.casefold)
    with open("sorted_words.txt", "w", encoding="utf-8") as output:
        output.write("\n".join(words) + ("\n" if words else ""))
    print("Sorted words saved to sorted_words.txt.")
except FileNotFoundError:
    print("sample.txt not found.")
