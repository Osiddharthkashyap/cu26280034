import sqlite3
# Select students whose marks are strictly greater than 80.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students WHERE marks > ? ORDER BY marks DESC", (80,)
        ).fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No students scored above 80.")
except sqlite3.Error as error:
    print("Database error:", error)
