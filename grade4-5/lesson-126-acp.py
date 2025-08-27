# Full Calculator Program

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result of addition:", num1 + num2)
elif choice == 2:
    print("Result of subtraction:", num1 - num2)
elif choice == 3:
    print("Result of multiplication:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result of division:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice! Please select between 1 and 4.")
