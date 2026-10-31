import csv
# Search names without case sensitivity.
try:
    target = input("Student name: ").strip().casefold()
    with open("students.csv", newline="", encoding="utf-8") as file:
        matches = [row for row in csv.DictReader(file)
                   if row.get("name", "").casefold() == target]
    if matches:
        for row in matches:
            print(row)
    else:
        print("No matching student found.")
except FileNotFoundError:
    print("students.csv not found.")
