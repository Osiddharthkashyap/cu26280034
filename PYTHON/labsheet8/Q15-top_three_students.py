import sqlite3
# Return at most three students with the highest marks.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students ORDER BY marks DESC, name LIMIT 3"
        ).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
