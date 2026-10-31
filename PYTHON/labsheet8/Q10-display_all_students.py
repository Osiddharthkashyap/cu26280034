import sqlite3
# Fetch and display all student records.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT id, name, age, marks FROM students ORDER BY id"
        ).fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No student records.")
except sqlite3.Error as error:
    print("Database error:", error)
