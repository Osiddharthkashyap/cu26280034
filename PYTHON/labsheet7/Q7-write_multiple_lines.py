# Accept lines until the user enters a blank line.
try:
    print("Enter lines; press Enter on an empty line to finish.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + ("\n" if lines else ""))
    print(f"Saved {len(lines)} line(s) to sample.txt.")
except OSError as error:
    print(f"File error: {error}")
