import sqlite3
# Count all rows in students.
try:
    with sqlite3.connect("student_db.db") as connection:
        total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total students:", total)
except sqlite3.Error as error:
    print("Database error:", error)
