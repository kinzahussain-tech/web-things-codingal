# Class to handle dictionary operations
class DictionaryLookup:
    def __init__(self):
        # Predefined dictionary
        self.data = {
            "name": "Kinza",
            "age": 25,
            "country": "Pakistan",
            "profession": "Teacher"
        }

    # Method to get value by key
    def get_value(self, key):
        return self.data.get(key, "Key not found!")


# Create an object
lookup = DictionaryLookup()

# Take key input from user
user_key = input("Enter the key to find its value: ")

# Call method to get value
print("Value:", lookup.get_value(user_key))
