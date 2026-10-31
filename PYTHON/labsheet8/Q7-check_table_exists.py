import sqlite3
# Query sqlite_master to test whether a table exists.
try:
    with sqlite3.connect("student_db.db") as connection:
        result = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
            ("students",)
        ).fetchone()
    print("students table exists." if result else "students table does not exist.")
except sqlite3.Error as error:
    print("Database error:", error)
