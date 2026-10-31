import sqlite3
# Change a student's name using their ID.
try:
    student_id = int(input("Student ID: "))
    name = input("New name: ").strip()
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute(
            "UPDATE students SET name=? WHERE id=?", (name, student_id)
        )
    print("Name updated." if cursor.rowcount else "No student found with that ID.")
except ValueError:
    print("ID must be an integer.")
except sqlite3.Error as error:
    print("Database error:", error)
