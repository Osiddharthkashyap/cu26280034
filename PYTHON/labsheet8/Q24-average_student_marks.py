import sqlite3
# AVG returns NULL when the table has no rows.
try:
    with sqlite3.connect("student_db.db") as connection:
        average = connection.execute("SELECT AVG(marks) FROM students").fetchone()[0]
    print("Average marks:", f"{average:.2f}" if average is not None else "No records")
except sqlite3.Error as error:
    print("Database error:", error)
