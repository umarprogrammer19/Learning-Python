# File Handling in Python: A Comprehensive Example

# 1. Opening a File
# 'w' mode: Write to a file (creates the file if it doesn't exist)
# 'r' mode: Read from a file
# 'a' mode: Append to the file
# 'x' mode: Exclusive creation (fails if the file exists)
# 'b' mode: Binary mode (for binary files)

# Create a file and write to it
with open("example.txt", "w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.writelines(["This is line 3.\n", "This is line 4.\n"])

# 2. Read the file and print its content
with open("example.txt", "r") as f:
    content = f.read()
    print("--- Full Content ---")
    print(content)

# 3. Read the file line by line and print each line
with open("example.txt", "r") as f:
    print("--- Line by Line ---")
    for line in f:
        print(line, end="")  # Using end='' to avoid extra newline

# 4. Read a single line
with open("example.txt", "r") as f:
    print("\n--- Readline ---")
    print(f.readline(), end="")  # Reads the first line only

# 5. Read all lines into a list
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("\n--- Readlines ---")
    for line in lines:
        print(line, end="")  # Iterating over the list of lines

# 6. Append to the file
with open("example.txt", "a") as f:
    f.write("This is appended line 1.\n")
    f.write("This is appended line 2.\n")

# 7. Reading with seek and tell (pointer manipulation)
with open("example.txt", "r") as f:
    print("\n--- Seek and Tell ---")
    print("Current position:", f.tell())  # Shows the current pointer position
    print("First line:", f.readline(), end="")  # Reads the first line
    print("Current position:", f.tell())  # Position after reading the first line
    f.seek(0)  # Moves the pointer back to the start of the file
    print("After seek(0):", f.tell())  # Check the position again
    print("First line again:", f.readline(), end="")  # Reads the first line again

# 8. Demonstrating 'x' mode (exclusive creation)
try:
    with open("new_file.txt", "x") as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")


# 9. Copy file example (copying content from one file to another)
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            for line in src:
                dest.write(line)
            print(f"'{source}' successfully copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File not found '{source}'")
    except Exception as e:
        print(f"Error during copying: {e}")


copy_file("example.txt", "example_copy.txt")

# Output Examples:
# --- Full Content ---
# This is line 1.
# This is line 2.
# This is line 3.
# This is line 4.

# --- Line by Line ---
# This is line 1.
# This is line 2.
# This is line 3.
# This is line 4.

# --- Readline ---
# This is line 1.

# --- Readlines ---
# This is line 1.
# This is line 2.
# This is line 3.
# This is line 4.

# --- Seek and Tell ---
# Current position: 0
# First line: This is line 1.
# Current position: 16
# After seek(0): 0
# First line again: This is line 1.

# File Handling Best Practices:
# - Use 'with' statement to automatically close the file.
# - Always handle exceptions like FileNotFoundError, ValueError.
# - Use file modes appropriately (e.g., 'w' for writing, 'r' for reading).
