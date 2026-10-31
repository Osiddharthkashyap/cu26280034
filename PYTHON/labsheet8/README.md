# Lab Sheet 08 — Database Management

Contains 30 standalone Python solutions using Python's built-in `sqlite3` module (no external package required). All programs share `student_db.db` in the current working directory. Run Q2/Q3 first to create the database and `students` table. Run Q21 before the JOIN programs; assign `course_id` values in the students table to see matching INNER JOIN rows. Q27 expects `students_import.csv` with headers `id,name,age,marks`.

Run any program with `python Q<number>-<file_name>.py`. SQLite's `DELETE FROM` is used for Q20 because SQLite does not support `TRUNCATE TABLE`; the table schema is preserved.
