import sqlite3
DB = "student_db.db"

def setup():
    with sqlite3.connect(DB) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
            age INTEGER NOT NULL, marks REAL NOT NULL)""")

def add_student():
    values = (int(input("ID: ")), input("Name: ").strip(),
              int(input("Age: ")), float(input("Marks: ")))
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", values)
    print("Student added.")

def view_students():
    with sqlite3.connect(DB) as con:
        rows = con.execute("SELECT * FROM students ORDER BY id").fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No records.")

def update_student():
    sid = int(input("ID to update: "))
    marks = float(input("New marks: "))
    with sqlite3.connect(DB) as con:
        cur = con.execute("UPDATE students SET marks=? WHERE id=?", (marks, sid))
    print("Updated." if cur.rowcount else "ID not found.")

def delete_student():
    sid = int(input("ID to delete: "))
    with sqlite3.connect(DB) as con:
        cur = con.execute("DELETE FROM students WHERE id=?", (sid,))
    print("Deleted." if cur.rowcount else "ID not found.")

def main():
    setup()
    actions = {"1": add_student, "2": view_students,
               "3": update_student, "4": delete_student}
    while True:
        print("\\n1.Add  2.View  3.Update marks  4.Delete  5.Exit")
        choice = input("Choice: ").strip()
        if choice == "5":
            break
        try:
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Choose 1-5.")
        except ValueError:
            print("Please enter valid numeric values.")
        except sqlite3.Error as error:
            print("Database error:", error)

if __name__ == "__main__":
    try:
        main()
    except sqlite3.Error as error:
        print("Database error:", error)
