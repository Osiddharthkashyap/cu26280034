# Display lines numbered 2, 4, 6, ... (one-based numbering).
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            if number % 2 == 0:
                print(line, end="")
except FileNotFoundError:
    print("sample.txt not found.")
