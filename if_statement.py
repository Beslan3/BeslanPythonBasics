# Programming often involves examining a set of conditions and deciding which action to take based on those conditions.
# Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.

# == means a comparison. is 'a' == (equal) 'b' ?

cars = ['toyota', 'lexus', 'bmw', 'tesla']
for car in cars:
    print(f'In this iteration car="{car}"')
    if car == 'tesla': # if this condition is true, execute the following code:
        print('IF case: this is the code to be execute when car=tesla, i.e. when the expression returns True.')
        print(f'My favourite electric car is {car.upper()}')
        print('******************************')
    elif car == 'bmw': # within a loop, it means "also if... something is true, then do this"...
        print("ELIF: this block of code is executed because car =='tesla' returned false, and car=='bmw' returned True.")
        print(f'Oh man {car.upper()} is something right?')
        print('******************************')
    else: # otherwise, of none of the above conditions are true, then do this...
        print("ELSE: not tesla, not bmw, car =='tesla' >> False, car =='bmw' >> False, thats why we are executing this lines")
        print(f'Your current car is {car.title()}')
        print('******************************')
print("############# Completed #################")

# Conditional Expressions (that returns True/False), which you can use in if or elif statements(lines) :
# var == 'value1', value1 == value2 , 5 == 4 (always false case)
# True, false
# value1 < value2, value1 > value2, value1 <= value2, value1 != value2
# value in list, (if 5 in nums), if 6 is in range(10) meaning 0 to 9 = True,
# if 'a' is in 'book' = False

if True:
    print("what's up")

nums = [2, 4, 7, 6, 5, 98, 45]
if 5 in nums: # (means if there's 5 in the list, then do this...)
    print('yep, five is here')
elif 6 in nums: # means: 'else, if the 1st IF cond is not true, and there's 6 in the list, then do this.
    # will only execute if the 1st IF cond is not true (because it's not a loop)
    # if it was a loop, then both IF and ELIF would execute, because it would loop through all elements.
    print('6 is here')
else: # means if the 1st IF and then ELIF is also not true
    print('5 and 6 are not here')

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# *******************************************************************
print(171%2)


