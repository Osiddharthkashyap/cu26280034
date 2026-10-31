import csv
# Display only Name and Marks fields from the CSV.
try:
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not {"name", "marks"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain name and marks columns.")
        for row in reader:
            print(f"Name: {row['name']}, Marks: {row['marks']}")
except FileNotFoundError:
    print("students.csv not found.")
except ValueError as error:
    print(error)
