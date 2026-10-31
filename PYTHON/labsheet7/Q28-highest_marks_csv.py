import csv
# Find the student with the highest marks.
try:
    with open("students.csv", newline="", encoding="utf-8") as file:
        students = list(csv.DictReader(file))
    valid = [(float(row["marks"]), row) for row in students if row.get("marks")]
    if not valid:
        print("No student marks found.")
    else:
        marks, student = max(valid, key=lambda item: item[0])
        print(f"Highest: {student.get('name', 'Unknown')} - {marks:g}")
except FileNotFoundError:
    print("students.csv not found.")
except (ValueError, KeyError) as error:
    print(f"Invalid CSV data: {error}")
