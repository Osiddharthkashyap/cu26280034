import sqlite3
# INNER JOIN displays only students assigned to a matching course.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("""
            SELECT s.id, s.name, c.course_name
            FROM students AS s
            INNER JOIN courses AS c ON s.course_id = c.id
            ORDER BY s.id
        """).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error (run Q21 to create courses):", error)
