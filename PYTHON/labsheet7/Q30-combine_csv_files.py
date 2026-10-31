import csv
# Combine CSV files with matching headers, writing the header once.
files = ["students.csv", "students_extra.csv"]
try:
    combined = []
    header = None
    for filename in files:
        with open(filename, newline="", encoding="utf-8") as source:
            reader = csv.reader(source)
            current_header = next(reader, None)
            if current_header is None:
                continue
            if header is None:
                header = current_header
            elif current_header != header:
                raise ValueError(f"Header mismatch in {filename}.")
            combined.extend(reader)
    with open("combined_students.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        if header:
            writer.writerow(header)
        writer.writerows(combined)
    print(f"Combined {len(combined)} data row(s) into combined_students.csv.")
except FileNotFoundError as error:
    print(f"Input file not found: {error.filename}")
except (OSError, ValueError) as error:
    print(f"Error: {error}")
