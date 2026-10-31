import csv
# Copy all CSV rows to a second CSV file.
try:
    with open("students.csv", newline="", encoding="utf-8") as source:
        rows = list(csv.reader(source))
    with open("students_copy.csv", "w", newline="", encoding="utf-8") as target:
        csv.writer(target).writerows(rows)
    print("Copied data to students_copy.csv.")
except FileNotFoundError:
    print("students.csv not found.")
