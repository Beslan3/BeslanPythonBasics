print("==== Variables ====")
# primitive (simple) data types:

# * STRING (text)
# * INTEGER (real number: 52, 4, 78)
# * BOOLEAN (yes/no)
# * FLOAT (floating point numbers: decimal values or fractional numbers like 13.5 , 287.11 , or 371.213

# VARIABLES: container to hold the value

# OBJECT - abstract data

# values covered with quotes (' ', "") considered as String data type

age = 10  # declaring the variable 'age', defining variable (set a value 10)
age = 15  # resetting the value of the variable

# NOTEs for using the variables:
# best practice: name your variable with meaningful name
# rule: you can not start variable name with number, name must start with letter
# rule: no space in variable name, instead you can '_' -> my_friend
# rule: start with lower case and use lowercase letters

# printing multiple values with print function
print(23, 242, 23, 'hello', True)

my_name = 'jameS broWn'  # string value (text data type)
my_age = 20  # integer value (numbers)
am_i_cool = True  # boolean data type (True/False)



first_name = 'janE    '
last_name = '    dOE'
# create a var by concatenating other vars:
full_name = (first_name.strip() + ' ' + last_name.strip()).title() # this is concatenating

print('------------------------------')
print('Hello, my name is', my_name)
print('thank you, this was', my_name, 'speaking with you tonight.')
print('if you have a comments please address it to', my_name)
print('I am', my_age, 'years old')
print('I will be', my_age + 5, 'years old in 5 years.')

print('------- string variables: built-in functions  -----------')
# .upper(), .lower(), .title()
print('UPPER()-convert to upper case, LOWER()-lower case, TITLE()-title each word')
print('Hello, my name is', my_name.upper())
print('thank you, this was', my_name.title(), 'speaking with you tonight.')
print('if you have a comments please address it to', my_name.lower())
# concatenation (adding +)
print('Full name (concatenate):', first_name.title() + ' ' + last_name.title())
print('Full name (concatenate):', (first_name + ' ' + last_name).title())
print('Full name (concatenate):', full_name)

print('------- Number variables: built-in operations  -----------')
# PLUS as + , MINUS as - , DIVISION as / , MULTIPLICATION as * , FLOOR DIVISION as // , MODULO as %
print('my ages is', my_age)
print("I'l be", my_age + 6, "in 6 years")
print('I was', my_age - 6, '6 years ago')
print('division 20 by 3 gives us', my_age / 3)
print('multiplication 20 by 3 gives us', my_age * 3)
print('floor division 20 by 3 gives us', my_age // 3)  # 20/3 = 6.6 = 6 (how many 3s in 20)
print('modulo 20 by 3 gives us', my_age % 3)  # 20/3 = (6*3)+2 = 2 (what remains after dividing 20/3)
# modulo is what remains after division.

# remove whitespace using functions: .strip(), .rs(), .ls()
first_name = 'janE  '
last_name = '  doE'
print('--------- removing white space by using functions such as: .strip(), .rs(), .ls() ')
print('Full name (concatenate):', first_name + ' ' + last_name)
# code to remove whitespace:
print('Full name (concatenate):', (first_name.strip() + ' ' + last_name.strip()).title())

# h/w:
print('homework -----------------------------------')
print(2 + 6)
print(2 * 4)
print(16 / 2)
print(9 - 1)
# ctrl + alt + l formats your code nicely
favorite_number = 3
print('my favorite number is', favorite_number)

# To add a newline in a string, use the character combination \n:
print("Python\nJava\nJavaScript") # \n means start a new line
# prints:
# Python
# Java
# JavaScript