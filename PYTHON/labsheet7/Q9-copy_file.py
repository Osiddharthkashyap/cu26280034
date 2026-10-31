import shutil
# Copy source text file to a destination file.
try:
    shutil.copyfile("sample.txt", "sample_copy.txt")
    print("Copied sample.txt to sample_copy.txt.")
except FileNotFoundError:
    print("Source file sample.txt not found.")
except OSError as error:
    print(f"File error: {error}")
