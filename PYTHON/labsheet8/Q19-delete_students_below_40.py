import sqlite3
# Delete all students whose marks are below 40.
try:
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("DELETE FROM students WHERE marks < ?", (40,))
    print(f"Deleted {cursor.rowcount} student(s) with marks below 40.")
except sqlite3.Error as error:
    print("Database error:", error)
