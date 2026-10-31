import sqlite3
# Delete one student by primary key.
try:
    student_id = int(input("Student ID to delete: "))
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (student_id,))
    print("Student deleted." if cursor.rowcount else "No student found.")
except ValueError:
    print("ID must be an integer.")
except sqlite3.Error as error:
    print("Database error:", error)
