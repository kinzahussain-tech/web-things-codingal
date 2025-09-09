# Function to check Disarium number
def is_disarium(num):
    # Convert number to string to get positions
    digits = str(num)
    length = len(digits)
    
    # Calculate sum of digits powered with their positions
    total = 0
    for i in range(length):
        total += int(digits[i]) ** (i+1)
    
    # Check condition
    return total == num


# Main program
n = int(input("Enter a number: "))

if is_disarium(n):
    print(n, "is a Disarium number.")
else:
    print(n, "is NOT a Disarium number.")
