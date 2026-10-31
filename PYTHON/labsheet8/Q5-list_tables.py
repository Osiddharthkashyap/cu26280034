import sqlite3
# List user-created tables in the connected SQLite database.
try:
    with sqlite3.connect("student_db.db") as connection:
        tables = connection.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name
        """).fetchall()
    print("Tables:", [row[0] for row in tables])
except sqlite3.Error as error:
    print("Database error:", error)
