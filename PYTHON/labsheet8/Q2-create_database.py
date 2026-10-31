import sqlite3
# Opening a connection creates the SQLite database if needed.
try:
    connection = sqlite3.connect("student_db.db")
    connection.close()
    print("Database student_db.db created or already exists.")
except sqlite3.Error as error:
    print("Database error:", error)
