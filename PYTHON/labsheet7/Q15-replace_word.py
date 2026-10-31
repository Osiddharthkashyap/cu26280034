import re
# Replace every whole-word occurrence and save the updated content.
try:
    old = input("Word to replace: ").strip()
    new = input("Replacement word: ")
    if not old:
        raise ValueError("The word to replace cannot be empty.")
    with open("sample.txt", encoding="utf-8") as file:
        content = file.read()
    updated, count = re.subn(rf"\b{re.escape(old)}\b", lambda _: new, content, flags=re.IGNORECASE)
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(updated)
    print(f"Replaced {count} occurrence(s).")
except FileNotFoundError:
    print("sample.txt not found.")
except (OSError, ValueError) as error:
    print(f"Error: {error}")
