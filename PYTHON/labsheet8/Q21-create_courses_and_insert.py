import sqlite3
# Create courses and link students to courses through course_id.
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                course_name TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                age INTEGER NOT NULL, marks REAL NOT NULL,
                course_id INTEGER REFERENCES courses(id)
            )
        """)
        connection.executemany(
            "INSERT OR IGNORE INTO courses(id, course_name) VALUES (?, ?)",
            [(1, "Python"), (2, "Database"), (3, "Web Development")]
        )
        # Add course_id to an older students table when this lab's Q3 created it.
        cols = {row[1] for row in connection.execute("PRAGMA table_info(students)")}
        if "course_id" not in cols:
            connection.execute("ALTER TABLE students ADD COLUMN course_id INTEGER REFERENCES courses(id)")
    print("courses table and sample courses are ready.")
except sqlite3.Error as error:
    print("Database error:", error)
