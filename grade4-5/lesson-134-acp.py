# Step 1: Create a file first
f = open("students.txt", "w")
f.write("Line 1: Hello Students!\n")
f.write("Line 2: Welcome to Python file handling.\n")
f.write("Line 3: This is an example file.\n")
f.write("Line 4: Enjoy learning!\n")
f.close()
print("File 'students.txt' created successfully!\n")


# Step 2.1: Read entire content at once
print("--- Reading with read() ---")
f = open("students.txt", "r")
print(f.read())
f.close()


# Step 2.2: Read only first 10 characters
print("\n--- Reading first 10 characters ---")
f = open("students.txt", "r")
print(f.read(10))
f.close()


# Step 2.3: Read line by line using readline()
print("\n--- Reading line by line with readline() ---")
f = open("students.txt", "r")
print(f.readline())   # reads first line
print(f.readline())   # reads second line
f.close()


# Step 2.4: Read all lines into a list using readlines()
print("\n--- Reading all lines with readlines() ---")
f = open("students.txt", "r")
lines = f.readlines()
print(lines)  # prints as a list
f.close()


# Step 2.5: Loop through file directly
print("\n--- Reading using loop ---")
f = open("students.txt", "r")
for line in f:
    print(line, end="")  # end="" prevents extra blank lines
f.close()
