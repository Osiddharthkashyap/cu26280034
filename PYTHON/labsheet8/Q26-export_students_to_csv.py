import sqlite3
import csv
# Export table headings and rows to students_export.csv.
try:
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("SELECT id, name, age, marks FROM students")
        rows = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
    with open("students_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Exported {len(rows)} record(s) to students_export.csv.")
except (sqlite3.Error, OSError) as error:
    print("Error:", error)
