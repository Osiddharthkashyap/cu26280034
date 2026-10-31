import sqlite3
# SQLite creates the database file automatically if it does not exist.
try:
    with sqlite3.connect("student_db.db") as connection:
        print("Connected to student_db.db successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
