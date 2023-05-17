class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        # long_name = str(self.year) + ' ' + self.make + ' ' + self.model (this was from book)
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's milage."""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if iit attempts to roll back the odometer reading.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage # modified attr-ute's value through a method
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't input a negative number!")
        else:
            self.odometer_reading += miles # += here means add to the value of miles to odometer reading.
# += operator adds two values together and assigns the final value to a variable.

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23 # Modifying an Attribute’s Value Directly through an INSTANCE
# my_new_car.read_odometer()

my_used_car = Car('subaru', "outback", 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-1)
my_used_car.read_odometer()


# Modifying an Attribute’s Value Through a METHOD:
# to do so, you'll need to write a new method that updates attributes for you:
# def update_odometer(self): ... see line 19

# my_new_car.update_odometer(22)