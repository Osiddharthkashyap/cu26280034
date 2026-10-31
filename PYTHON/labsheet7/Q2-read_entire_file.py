from pathlib import Path
# Read and display the complete contents of a text file.
try:
    print(Path("sample.txt").read_text(encoding="utf-8"))
except FileNotFoundError:
    print("sample.txt not found. Run Q1 first or create the file.")
except OSError as error:
    print(f"File error: {error}")
