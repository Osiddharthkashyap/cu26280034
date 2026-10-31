# Read whitespace-separated numeric values from numbers.txt.
try:
    with open("numbers.txt", encoding="utf-8") as file:
        numbers = [float(value) for value in file.read().split()]
    if not numbers:
        print("The file contains no numbers.")
    else:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
except FileNotFoundError:
    print("Create numbers.txt with numeric values separated by spaces or lines.")
except ValueError as error:
    print(f"Invalid numeric data: {error}")
