import csv
# Read and display all rows from students.csv.
try:
    with open("students.csv", newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            print(" | ".join(row))
except FileNotFoundError:
    print("students.csv not found. Run Q21 first.")
