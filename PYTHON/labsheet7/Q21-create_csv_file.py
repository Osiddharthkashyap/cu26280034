import csv
# Create a CSV file containing student records.
records = [
    ["id", "name", "age", "marks"],
    [1, "Asha", 20, 88],
    [2, "Ravi", 21, 76],
    [3, "Neha", 20, 93],
]
try:
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(records)
    print("Created students.csv with sample records.")
except OSError as error:
    print(f"CSV error: {error}")
