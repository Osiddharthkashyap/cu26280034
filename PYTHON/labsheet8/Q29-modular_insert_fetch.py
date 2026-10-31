import sqlite3
DB = "student_db.db"

def insert_student(student_id, name, age, marks):
    # Parameterized insert is safe for user-provided values.
    with sqlite3.connect(DB) as connection:
        connection.execute(
            "INSERT INTO students(id, name, age, marks) VALUES (?, ?, ?, ?)",
            (student_id, name, age, marks)
        )

def fetch_students():
    # Return all student rows to the caller.
    with sqlite3.connect(DB) as connection:
        return connection.execute("SELECT * FROM students ORDER BY id").fetchall()

try:
    insert_student(int(input("ID: ")), input("Name: ").strip(),
                   int(input("Age: ")), float(input("Marks: ")))
    print("Inserted. Current students:")
    for student in fetch_students():
        print(student)
except ValueError:
    print("Invalid numeric input.")
except sqlite3.Error as error:
    print("Database error:", error)
