# Program to print power series

# Take input from user
x = int(input("Enter the base number (x): "))
n = int(input("Enter number of terms (n): "))

print(f"Power series of {x} up to {n} terms:")

for i in range(1, n+1):
print(x**i, end=" ")