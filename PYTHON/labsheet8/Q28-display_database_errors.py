import sqlite3
# Deliberately execute an invalid query to demonstrate exception handling.
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("SELECT * FROM table_that_does_not_exist")
except sqlite3.Error as error:
    print("SQLite database error caught:", error)
