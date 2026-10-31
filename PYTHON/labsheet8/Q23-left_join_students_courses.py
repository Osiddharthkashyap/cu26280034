import sqlite3
# LEFT JOIN includes students even when they have no assigned course.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("""
            SELECT s.id, s.name, c.course_name
            FROM students AS s
            LEFT JOIN courses AS c ON s.course_id = c.id
            ORDER BY s.id
        """).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error (run Q21 to create courses):", error)
