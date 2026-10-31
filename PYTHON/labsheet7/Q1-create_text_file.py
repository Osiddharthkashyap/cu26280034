from pathlib import Path
# Create a text file and write user-provided content.
try:
    content = input("Enter text to write: ")
    Path("sample.txt").write_text(content + "\n", encoding="utf-8")
    print("Text written to sample.txt successfully.")
except OSError as error:
    print(f"File error: {error}")
