import sqlite3
# Group students by age and count the members in each group.
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("""
            SELECT age, COUNT(*) FROM students GROUP BY age ORDER BY age
        """).fetchall()
    for age, count in rows:
        print(f"Age {age}: {count} student(s)")
except sqlite3.Error as error:
    print("Database error:", error)
