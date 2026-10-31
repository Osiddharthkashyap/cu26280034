import sqlite3
# Sort student records by marks from highest to lowest.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students ORDER BY marks DESC, name"
        ).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
