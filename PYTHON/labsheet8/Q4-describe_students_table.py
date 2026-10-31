import sqlite3
# PRAGMA table_info returns each column's name, type and constraints.
try:
    with sqlite3.connect("student_db.db") as connection:
        columns = connection.execute("PRAGMA table_info(students)").fetchall()
    if not columns:
        print("students table does not exist.")
    else:
        print("cid | name | type | notnull | default | primary_key")
        for column in columns:
            print(column)
except sqlite3.Error as error:
    print("Database error:", error)
