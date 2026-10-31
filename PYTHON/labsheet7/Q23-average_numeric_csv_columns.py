import csv
# Calculate averages for columns whose non-empty values are numeric.
try:
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = {}
        for row in reader:
            for key, value in row.items():
                try:
                    columns.setdefault(key, []).append(float(value))
                except (TypeError, ValueError):
                    continue
    if not columns:
        print("No numeric columns found.")
    for name, values in columns.items():
        print(f"{name} average: {sum(values) / len(values):.2f}")
except FileNotFoundError:
    print("students.csv not found.")
