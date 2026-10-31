import csv
# Append one student record to students.csv.
try:
    student_id = input("ID: ").strip()
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with open("students.csv", "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([student_id, name, age, marks])
    print("Record appended.")
except FileNotFoundError:
    print("students.csv not found; run Q21 first.")
except ValueError:
    print("Age must be an integer and marks must be numeric.")
