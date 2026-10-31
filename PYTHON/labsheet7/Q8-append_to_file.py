# Append a new line without removing existing file contents.
try:
    text = input("Enter text to append: ")
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print("Content appended.")
except OSError as error:
    print(f"File error: {error}")
