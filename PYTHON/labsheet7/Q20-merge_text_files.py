# Merge file1.txt and file2.txt into merged.txt.
try:
    with open("merged.txt", "w", encoding="utf-8") as output:
        for filename in ("file1.txt", "file2.txt"):
            with open(filename, encoding="utf-8") as source:
                content = source.read()
            output.write(content)
            if content and not content.endswith("\n"):
                output.write("\n")
    print("Merged file1.txt and file2.txt into merged.txt.")
except FileNotFoundError as error:
    print(f"Input file not found: {error.filename}")
except OSError as error:
    print(f"File error: {error}")
