# Creating a Car class
class Car:
    # Constructor (attributes)
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method (behavior)
    def start(self):
        print(f"The {self.color} {self.brand} is starting!")

    def stop(self):
        print(f"The {self.color} {self.brand} has stopped.")

# Creating objects (real cars)
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Calling methods (behaviors)
car1.start()
car2.stop()