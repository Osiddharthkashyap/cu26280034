# Display the longest line; ties are resolved by the first occurrence.
try:
    with open("sample.txt", encoding="utf-8") as file:
        lines = file.readlines()
    if not lines:
        print("The file is empty.")
    else:
        longest = max(lines, key=len)
        print("Longest line:", longest.rstrip("\n"))
        print("Character count:", len(longest.rstrip("\n")))
except FileNotFoundError:
    print("sample.txt not found.")
