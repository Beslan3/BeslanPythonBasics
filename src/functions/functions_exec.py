# Functions execution file

# module, package, import

# path: ./src/functions/functions.py -> greet_user_by_name()
# from src.functions.functions import greet_user_by_name, greet_user, thank_you_by_name # import one by one
# import line reads and execute the file
from src.functions.functions import greet_user_by_name, thank_you_by_name
# you can use alias name for the imported function
from src.functions.functions import greet_user as greet
from src.functions.functions_return import * # import all
print('******************EXECUTION:')
greet_user_by_name('john')
greet()
greet_user_by_name('jane')
greet()
greet_user_by_name('britney')
thank_you_by_name('john', 10)
thank_you_by_name('jane', 5)
thank_you_by_name('britney', 20)
thank_you_by_name('mark', 1)

print("Executing the functions with Keyword Arguments (not Positional Arguments).")
print(get_full_name(fistname='jane', middlename='rogers', lastname='doe'))
print(get_full_name('anne', 'doe', 'marie'))
print(get_full_name(456, 'asdf', 000))

print_all_names(['james', 'salah', 'michael'])
# h/w : 8-9, 8-10, 8-11

thank_you_by_name('mark', 20)
cars = ['lexus', 'tesla', 'bmw']
print_all_names(cars)
