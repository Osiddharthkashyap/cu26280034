import csv
# Count data rows and header columns.
try:
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
    if not rows:
        print("CSV file is empty.")
    else:
        print("Number of columns:", len(rows[0]))
        print("Number of data rows:", max(0, len(rows) - 1))
except FileNotFoundError:
    print("students.csv not found.")
