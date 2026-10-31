# Remove lines that contain only whitespace.
try:
    with open("sample.txt", encoding="utf-8") as file:
        lines = file.readlines()
    kept = [line for line in lines if line.strip()]
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.writelines(kept)
    print(f"Removed {len(lines) - len(kept)} blank line(s).")
except FileNotFoundError:
    print("sample.txt not found.")
except OSError as error:
    print(f"File error: {error}")
