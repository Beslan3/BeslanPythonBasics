class Car:
    """Blueprint to represent the general car."""
    # '__' hides attribute from object. makes it private
    # so attributes are not available outside the class (objects are outside)

    # Constructor (__init__ - silent method)
    def __init__(self, make, model, year):
        self.__make = make # the '__' hides attribute from object. private.
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0 # default value
        # __ hides attribute from object, so attributes are not available outside the class (objects are outside)
        # in Java: 'private this.odometer_reading = 0'

    def get_description(self):
        """summary of the car details, usually you have return statement"""
        print(f"Details of the car\nMake/model/year: {self.__make.title()}/{self.__model.upper()}/{self.__year}")
    def get_odometer(self):
        return f'Current milage: {self.__odometer_reading}'

    def set_odometer(self, milage):
        """updates the odometer reading to a given milage"""
        print('updating the odometer reading:')
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f'invalid milage was entered for the odometer! value entered: {milage}')
        self.__odometer_reading = milage

    def increment_odometer(self, miles:int):
        print(f'adding {miles} mile to your odometer reading...')
        if miles > 0:
            self.__odometer_reading += miles
        else:
            print(f'miles should be positive number! value entered: {miles}')


# create the object (instance of Car class):
car1 = Car('toyota', 'hgihlander', 2023)
car1.get_description()
# print(car1.__model) # you can do before hiding
# print('car1.odometer_reading:', car1.__odometer_reading)
print('------------')
print(car1.get_odometer())
car1.set_odometer(10000)
print(car1.get_odometer())
# car1.__odometer_reading = 5000 # does the same job as car1.set_odometer()

# How to restrict object updating attributes directly, so we can only set odometer using the function
# OOP concept - encapsulation, hide the attributes from the object (or child classes)
# access modifier in java -> private
print(car1.get_odometer())
car1.set_odometer(1000) # testing the logic here

car1.set_odometer(20000) # testing the logic here
print(car1.get_odometer())
car1.increment_odometer(50)
car1.get_odometer()
print(car1.get_odometer())
# car1.increment_odometer('a')
car1.increment_odometer(-50)
print(car1.get_odometer())
# h.w: 945, 9-5

