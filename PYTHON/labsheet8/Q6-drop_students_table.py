import sqlite3
# Drop the students table after explicit confirmation.
try:
    answer = input("Type YES to permanently drop students table: ")
    if answer == "YES":
        with sqlite3.connect("student_db.db") as connection:
            connection.execute("DROP TABLE IF EXISTS students")
        print("students table dropped.")
    else:
        print("Cancelled; no table was dropped.")
except sqlite3.Error as error:
    print("Database error:", error)
