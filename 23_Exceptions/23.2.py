import sys

def open_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File content:")
        print(content)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except IOError:
        print("Error: Could not read the file.")
        sys.exit(1)

# Trying to open a file
file_name = "example.txt"  # Replace with the name of an existing file or a non-existing file to test
open_file(file_name)
