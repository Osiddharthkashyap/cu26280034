import sqlite3
# Insert one student using placeholders to avoid SQL injection.
try:
    student_id = int(input("ID: "))
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect("student_db.db") as connection:
        connection.execute(
            "INSERT INTO students(id, name, age, marks) VALUES (?, ?, ?, ?)",
            (student_id, name, age, marks)
        )
    print("Student inserted.")
except ValueError:
    print("Enter a valid integer ID/age and numeric marks.")
except sqlite3.Error as error:
    print("Database error (create students table first):", error)
