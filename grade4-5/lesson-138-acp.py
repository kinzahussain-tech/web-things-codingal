import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

print("=== Dice Rolling Simulator ===")

while True:
    print("\n1. Roll the Dice")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    # Conditional statements
    if choice == '1':
        dice_value = roll_dice()
        print(f"🎲 You rolled: {dice_value}")
    elif choice == '2':
        print("Exiting... Thanks for playing!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")
