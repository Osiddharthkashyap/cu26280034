import sqlite3
# Create the common students table if it does not already exist.
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                marks REAL NOT NULL
            )
        """)
    print("students table is ready.")
except sqlite3.Error as error:
    print("Database error:", error)
