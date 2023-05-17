# Chapter 9 : Functions
# function name is the summary of the action it does
# keep your functions to do specific task only (recommended)
# function names should not have space, use '_' (underscore) instead
# docstring to describe functions, parameter and give example of execution

def greet_user():
    """Display a simple greetings"""
    # pass  # do nothing but keeps the syntax of the functions
    print('Hello!!')


def greet_user_by_name(name):
    """
    Display a simple greetings by using the name
    :param name: pass the name you wanted to use in greetings
    :return: nothing
    """
    print(f'Hello, {name.title()}!!')


def thank_you_by_name(name, years):
    """ Display thank you message"""
    print(f'Thank you {name.title()} for being with us {years} years')


print("I am free of any function")


