# Activity: File Access Modes in Python

# Step 1: Write Mode (w) - creates new file / overwrites existing one
print("\n--- Step 1: Write Mode (w) ---")
f = open("myfile.txt", "w")
f.write("Hello Students!\n")
f.write("This is the first line in the file.\n")
f.close()
print("File created and data written successfully!")


# Step 2: Read Mode (r) - read file content
print("\n--- Step 2: Read Mode (r) ---")
f = open("myfile.txt", "r")
content = f.read()
print("File content:\n", content)
f.close()


# Step 3: Append Mode (a) - add new data without removing old
print("\n--- Step 3: Append Mode (a) ---")
f = open("myfile.txt", "a")
f.write("This line is added later using append mode.\n")
f.close()
print("New line appended successfully!")

# Read back to check
f = open("myfile.txt", "r")
print("File content now:\n", f.read())
f.close()


# Step 4: Read + Write Mode (r+)
print("\n--- Step 4: Read + Write Mode (r+) ---")
f = open("myfile.txt", "r+")
print("Before modification:\n", f.read())
f.seek(0)   # Move to start
f.write("Modified first line!\n")
f.close()

# Read back to check
f = open("myfile.txt", "r")
print("After modification:\n", f.read())
f.close()


# Step 5: Write + Read Mode (w+)
print("\n--- Step 5: Write + Read Mode (w+) ---")
f = open("myfile.txt", "w+")
f.write("This will erase previous content!\n")
f.seek(0)
print("File content after w+:\n", f.read())
f.close()


# Step 6: Append + Read Mode (a+)
print("\n--- Step 6: Append + Read Mode (a+) ---")
f = open("myfile.txt", "a+")
f.write("Another line added with a+ mode.\n")
f.seek(0)
print("File content after a+:\n", f.read())
f.close()
