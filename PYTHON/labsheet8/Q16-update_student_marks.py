import sqlite3
# Update marks for the supplied student ID.
try:
    student_id = int(input("Student ID: "))
    marks = float(input("New marks: "))
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute(
            "UPDATE students SET marks=? WHERE id=?", (marks, student_id)
        )
    print("Marks updated." if cursor.rowcount else "No student found with that ID.")
except ValueError:
    print("ID and marks must be numeric.")
except sqlite3.Error as error:
    print("Database error:", error)
