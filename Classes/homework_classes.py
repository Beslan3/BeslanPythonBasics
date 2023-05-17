# H/W:
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is a {self.restaurant_name.title()} and the cuisine is {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f'The restaurant is open')

    def set_number_served(self, customers):
        if customers < 0:
            print("You can't input a negative number!")
        else:
            self.number_served = customers

    def increment_number_served(self, added_customers):
        if added_customers < 0:
            print("You can't input a negative number!")
        else:
            self.number_served += added_customers # += here means add to the value of added_cust to number_ser


restaurant = Restaurant("sushi Restaurant", "japanese")
print(f'\nNumber of customers served is {restaurant.number_served} (number_served default)')
restaurant.number_served = 12
print(f'Number of customers served is {restaurant.number_served} (number_served = 12)')
restaurant.set_number_served(16)
print(f'Number of customers served is {restaurant.number_served} (set.number_served(16) )')
restaurant.increment_number_served(3)
print(f'Number of customers served is {restaurant.number_served} (increment_number_served(3) ) ')

# print("My restaurant name is " + restaurant.restaurant_name)
# print(f"This restaurant is of {restaurant.cuisine_type} ")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# second_restaurant = Restaurant("mcDonald's", "junk food")
# second_restaurant.describe_restaurant()
#
# third_restaurant = Restaurant("organic restaurant", "healthy food")
# third_restaurant.describe_restaurant()

# ********************************************************************************
class User():
    def __init__(self, first_name, last_name, height, weight, email_address):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.height = height
        self.weight = weight
        self.email_address = email_address
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser's name is {self.first_name} {self.last_name}. His height is {self.height}. The weight of the user is {self.weight} and their email address is {self.email_address}")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
    def increment_attempts(self):
        self.login_attempts += 1 # += here means add 1 to login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0 # resets the value of login_attempts to 0
    def count_login_attempts(self):
        print(f'Number of login attempts: {str(self.login_attempts)}')

# Make an instance of the User class and call increment_login_attempts() several times.
user_1 = User("Michael", "Jackson", "5'11" , "160 lbs", "mjack@gmail.com")
user_1.increment_attempts()
user_1.increment_attempts()
user_1.increment_attempts()
user_1.count_login_attempts()

# then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
user_1.reset_login_attempts()
user_1.count_login_attempts()

user_2 = User("Bill", "Gates", "5'8", "150 lbs", "bgates@gmail.com")
# user_2.describe_user()
# user_2.greet_user()
#