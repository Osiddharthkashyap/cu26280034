# Count whitespace-separated words in a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        word_count = sum(len(line.split()) for line in file)
    print("Number of words:", word_count)
except FileNotFoundError:
    print("sample.txt not found.")
