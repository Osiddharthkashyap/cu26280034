# Display the first and last lines (only once if there is one line).
try:
    with open("sample.txt", encoding="utf-8") as file:
        lines = file.readlines()
    if not lines:
        print("The file is empty.")
    else:
        print("First line:", lines[0].rstrip())
        print("Last line:", lines[-1].rstrip())
except FileNotFoundError:
    print("sample.txt not found.")
