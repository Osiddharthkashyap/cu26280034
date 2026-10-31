import sqlite3
import csv
# Import rows from CSV with columns id,name,age,marks.
try:
    with open("students_import.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        records = [(int(row["id"]), row["name"], int(row["age"]), float(row["marks"]))
                   for row in reader]
    with sqlite3.connect("student_db.db") as connection:
        connection.executemany(
            "INSERT INTO students(id, name, age, marks) VALUES (?, ?, ?, ?)",
            records
        )
    print(f"Imported {len(records)} record(s).")
except FileNotFoundError:
    print("Create students_import.csv with headers: id,name,age,marks")
except (ValueError, KeyError) as error:
    print("Invalid CSV data:", error)
except sqlite3.Error as error:
    print("Database error:", error)
