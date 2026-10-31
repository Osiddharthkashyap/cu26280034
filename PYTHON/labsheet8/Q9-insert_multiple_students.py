import sqlite3
# Insert several records in one transaction using executemany.
try:
    count = int(input("How many students? "))
    records = []
    for _ in range(count):
        records.append((
            int(input("ID: ")), input("Name: ").strip(),
            int(input("Age: ")), float(input("Marks: "))
        ))
    with sqlite3.connect("student_db.db") as connection:
        connection.executemany(
            "INSERT INTO students(id, name, age, marks) VALUES (?, ?, ?, ?)",
            records
        )
    print(f"Inserted {len(records)} student(s).")
except ValueError:
    print("Invalid numeric input.")
except sqlite3.Error as error:
    print("Database error:", error)
