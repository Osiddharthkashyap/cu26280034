import sqlite3
# Retrieve only the requested columns.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT name, marks FROM students ORDER BY name"
        ).fetchall()
    for name, marks in rows:
        print(f"{name}: {marks}")
except sqlite3.Error as error:
    print("Database error:", error)
