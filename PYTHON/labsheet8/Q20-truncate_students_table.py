import sqlite3
# SQLite has no TRUNCATE TABLE statement; DELETE removes rows and preserves schema.
try:
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("DELETE FROM students")
    print(f"Removed {cursor.rowcount} row(s); students table structure remains intact.")
except sqlite3.Error as error:
    print("Database error:", error)
