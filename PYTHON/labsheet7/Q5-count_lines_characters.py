# Count lines and characters (including newline characters).
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("Number of lines:", len(content.splitlines()))
    print("Number of characters:", len(content))
except FileNotFoundError:
    print("sample.txt not found.")
