# Read a text file one line at a time.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            print(f"{number}: {line.rstrip()}")
except FileNotFoundError:
    print("sample.txt not found.")
except OSError as error:
    print(f"File error: {error}")
