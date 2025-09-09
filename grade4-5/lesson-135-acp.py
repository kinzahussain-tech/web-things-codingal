# Activity: Working with Files in Python

# Step 1: Create & Write into a file
print("\n--- Step 1: Write Mode ---")
f = open("students.txt", "w")
f.write("Line 1: Hello Students!\n")
f.write("Line 2: Welcome to Python file handling.\n")
f.write("Line 3: Practice makes you perfect.\n")
f.write("Line 4: Enjoy learning!\n")
f.close()
print("File created and initial data written!\n")


# Step 2: Read the file
print("--- Step 2: Read File ---")
f = open("students.txt", "r")
print(f.read())
f.close()


# Step 3: Append new data
print("\n--- Step 3: Append Mode ---")
f = open("students.txt", "a")
f.write("Line 5: Keep up the good work!\n")
f.close()
print("New line appended.\n")

# Read again to verify
f = open("students.txt", "r")
print(f.read())
f.close()


# Step 4: Count total lines and words
print("\n--- Step 4: Count Lines & Words ---")
f = open("students.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))

f.seek(0)  # reset pointer
words = f.read().split()
print("Total words:", len(words))
f.close()


# Step 5: Update (overwrite first line)
print("\n--- Step 5: Update First Line ---")
f = open("students.txt", "r+")
data = f.readlines()
data[0] = "Line 1: UPDATED - Welcome Everyone!\n"
f.seek(0)
f.writelines(data)
f.close()
print("First line updated.\n")

# Final check
f = open("students.txt", "r")
print(f.read())
f.close()
