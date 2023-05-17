# Object - abstract data
# An object is simply a collection of data (variables) and methods (functions).

# Data structures: LIST ['v1', 'v2'], TUPLE (v1, v2), SET {v1, v2}, DICTIONARY {k:1v1, k2:v2}
# Operations: crate, read, update, delete (CRUD)
# Each DS has mostly used builtin functions

# LIST - meaning list of values - similar data types - separating with comma
# list covered with square brackets: ['value1', 'value2']

print('# CREATE *****************************************')
# creating empty lists (two options):
friends = []
nums = list() # list() is a functions that creates a list, or it can convert something to a list

# creating lists with values:
my_info = ['jane', 'doe', 30, 'dubai', True, '04/15/1993']
cities = ['brooklyn', 'manhattan', 'los angeles']

print('# READ *******************************************')
# INDEXING each element of the list (in order to access it)
print(my_info[0])  # jane
print(my_info[1])  # doe
print(my_info[-4]) # 30
print(my_info[-1]) # 04/15/1993
print(my_info[5])  # 04/15/1993
print(my_info[4])  # True
print(my_info[3])  # dubai
print(f'First element of my_info list is: {my_info[0]}')         # jane. with f string
print(f'First element of my_info list is: {my_info[0].title()}') # jane. with f string. with .title function applied
print(f'Last element of cities list is: {cities[-1].title()}')   # Los Angeles. with f string. with .title function applied
print(f'Last element of cities list is: {cities[2].title()}')    # Los Angeles. with f string. with .title function applied
print(f'{my_info[0].title()} will be {my_info[2] + 5} years old in 5 years.')

# creating a list from user INPUT
# inputs can accept values from the users (result is always a STRING, meaning text.)
# So if you want to treat it different way - you need to convert.

# so since age input will be treated as string, we need to convert it to int (in order to do adding, multiplying etc.)
# option 1: age = int(input('enter your age: '))
# option 2:
# name = input('enter your name: ')
# age = input('enter your age: ') # right side of the code after equal sign will be executed 1st and set as a new value to the age variable
# age = int(age) # here we are defining that whatever new numbers we put into the age input, it will be automatically converted into int.
# city = input('enter your city: ')
# user_info = [name, age, city] # this is the list, that will be made of data that the user inputs
# print(f'User info: {user_info}')
# print(f'Name of the user: {user_info[0].title()}')
# print(f'Age of the user 2 years ago: {user_info[1] - 2 }')
# print(f'Location of the user: {user_info[2].upper()}')

# UPDATING ----------------------------------------------
# INSERT, APPEND, replace element: select it by index and assign a new value cities[2] = 'new york'
print(' UPDATE +++++++++++++++++++++++++++++++++++++++++++')
# update means changing (updating) from original values, i.e. from whatever we first came up with.
print('original list of cities', cities) # ['brooklyn', 'manhattan', 'los angeles']

print("# Inserting/adding elements to the list -----------")
# INSERT: list_name.insert(1, 'houston') ADD ELEMENTS in specific place in list (will move the rest to the right):
cities.insert(1, 'houston') # this will add houston and move manhattan to the right (manhattan had index 1 before updating)
print('updated cities', cities) # now we have ['brooklyn', 'houston', 'manhattan', 'los angeles']

# APPEND: list_name.append('seattle') ADD NEW ELEMENT TO THE END OF THE LIST (APPEND):
cities.append('seattle') # append is mostly used in python. adds new element to the end of list
print('new city added to the list:', cities)
print(f'new city added to the list: {cities}') # 2-nd option of printing the list, does same thing
print(f'print specific element by its index: {cities [-1]} ') # print only seattle
print(f'print specific element by its index (another way): {cities [len(cities)-1]} ') # print only seattle

# REPLACE ELEMENTS IN THE LIST: cities[2] = 'new york'
print('# updating/replacing the existing element value (setting new value) ---')
cities[2] = 'new york' # this will set a new value (new york) to index 2 (used to be manhattan)
print('updated/replaced manhattan', cities) # thus we replaced manhattan w new york ['brooklyn', 'houston', 'new york', 'los angeles']

# ---------------------------------------------------------------
# FIND INDEX NUMBER by element's VALUE = list_name.index('value')
# (if you have a long list and don't know the exact index number)
print('find out index of houston by element value:', cities.index('houston')) # index() function
# so find out index number BY VALUE: list_name.index('element value')

# SEE HOW MANY ELEMENTS WE HAVE IN THE LIST:
print('counting the number of elements in cities list: ',len(cities)) # use function len(name of list) len means length

# DELETE ELEMENTS ----------------------------------------------------------
# del list_name[1] - deletes/removes element only by index. only deletes/removes.
# list_name.pop(1) - by index or no index. saves deleted el. if no index provided, will remove last element by default.
# list_name.remove('element value') -  removes elements by value (by element name)
print('# DELETE elements ---------------------------------------------------')
print('original before deleting:', cities)

# 1st DEL FUNCTION (only by index):
del cities[0]
print('after deleting the first element with del', cities) # now ['houston', 'new york', 'los angeles', 'seattle']

# 2nd .POP FUNCTION by (index or no index) -
deleted_city = cities.pop(2) # cities.pop(2) is the code to delete using pop() function
# deleted_city here is a new var we created to save the deleted el-nt. it will represent the deleted element.
print('after deleting the 3rd element (los angeles) with pop()', cities) # now ['houston', 'new york', 'seattle']
print('deleted city is', deleted_city) # thus we return/display the deleted element.

# 3rd  .REMOVE FUNCTION (by element value (name) ):
cities.remove('new york') # removing by value (removes 1st occurrence of the value:
# if you have 2 new yorks, it'll remove only the 1st one.
print('after deleting the new york element by its name with .remove()', cities) # ['houston', 'seattle']

print('---------this is the list created with list() function')
blbl = list('jane') # list() function
print(blbl)

# H/W:
print('HOMEWORK-------------------------------------')
# create a list of people you want to invite to dinner
dinner_list = ['John', 'Jane', 'Bob', 'Kelly']
# print a message to each person, inviting them to dinner.
print('Dear ', dinner_list, 'I would like to invite you all to dinner')
# print statement, stating the name of the guest who can’t make it
print('dear friends, unfortunately',dinner_list [2].title(), 'and', dinner_list[3].title(), 'can not make it to dinner')
# replace the name of the guest who can’t make it with the name of the new person you are inviting.
dinner_list[2] = 'Mike'
dinner_list[3] = 'Jessica'
# Print a second set of invitation messages
print('Dear friends', dinner_list, 'I would like to invite you all to a dinner')
# insert a new guest in the beginning of the list
dinner_list.insert(0, 'Alex')
print(f'inserted in the beginning {dinner_list}')
# Use insert() to add one new guest to the middle of your list
dinner_list.insert(2, 'Bob')
print(f'inserted in the middle list {dinner_list}')
# Use append() to add one new guest to the end of your list
dinner_list.append('Rebecca')
# Print a new set of invitation messages
print(f'Dear {dinner_list}, this is a new invitation with updated guest list')
# Add a new line that prints a message saying that you can invite only two people for dinner
print(f'Dear {dinner_list}, unfortunately I can not invite you all since there is space only for two guests')
# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite them to dinner
popped_guest_1 = dinner_list.pop(0)
print(f'dear {popped_guest_1}, unfortunately there is no space for you')
popped_guest_2 = dinner_list.pop(1)
print(f'dear {popped_guest_2}, unfortunately there is no space for you')
popped_guest_3 = dinner_list.pop(2)
print(f'dear {popped_guest_3}, unfortunately there is no space for you')
popped_guest_4 = dinner_list.pop(3)
print(f'dear {popped_guest_4}, unfortunately there is no space for you')
popped_guest_5 = dinner_list.pop() # no index provided here, so deleted the last element in the list
print(f'dear {popped_guest_5}, unfortunately there is no space for you')
# Print a message to each of the two people still on your list, letting them know they’re still invited
print(f'dear {dinner_list}, I am happy to invite you to dinner')
# removed element by its value using .remove(element value) function
dinner_list.remove('Jane')
print(f'removed Jane using .remove(element value) function, so the last name remaining is {dinner_list}')
# Use del to remove the last name from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.
del dinner_list[0]
print(f'removed the last name using del function {dinner_list}')

# -----------------------------------------------------
# SORTING IN LISTS

# 2 types of sorting: sorted(list_name) temporary, and list_name.sort() permanent

# sorted(list_name, reverse=True) # temporary sorting in DESCENDING order
# list_name.sort(reverse=True) # permanent sorting in DESCENDING order

print('Sorting in lists ------------------------------')
cars = ['lexus', 'bmw', 'toyota', 'tesla']
print(f'cars list: {cars}')

print("## temporary sorting of list with sorted() -----------")
print(f'sorted list with sorted(): {sorted(cars)}')
print(f'same list printed again: changes not saved: {cars}') # sorting will not be saved, cause temporary
print(f'sorted list with sorted(reverse=True): {sorted(cars, reverse=True)}')
print(f'same list after was sorted(): {cars}') # sorting will not be saved, cause temporary
# the result of sorted() function can be assigned to a new variable and saved
# so if you want to save it as a new separate variable, you can create it:
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars, reverse=True)
print(f'sorted_cars_asc: {sorted_cars_asc}')
print(f'sorted_cars_desc: {sorted_cars_desc}')
# so thus, instead of changing the original list permanently, we created a separate list
# like in example above with the new variable sorted_cars_asc or desc.

print("## permanent sorting of list with sort() -----------")
#cars.sort() # permanent sorting by default in ascending order.
#print(f'sorted cars list with sort(): {cars}')
cars.sort(reverse=True) # permanent sorting in descending order.
print(f'sorted cars list with sort(reverse=True): {cars}')
# if you append new element to the list, you'll need sort it again.
cars.append('honda')
print(f'cars after append: {cars}')

# problem-solving question: you have huge list of integers,
# how you can find smallest and largest number
nums = [4, 23, 6, 0, -11, 4567, 1234]

# solution 1
nums.sort() # permanent
print(f'sorted {nums}')
smallest_num1 = nums[0]
largest_num2 = nums[-1]
print(f'smallest num 1st solution: {smallest_num1}')
print(f'largest num 1st solution: {largest_num2}')
# solution 2
sorted_nums = sorted(nums) # since we made a new var, changes will be saved. otherwise would be temp.
smallest_num = sorted_nums[0]
largest_num = sorted_nums[-1]
print(sorted_nums)
print(f'smallest num 2nd solution: {smallest_num}')
print(f'largest num 2nd solution: {largest_num}')

# REVERSE FUNCTION: list_name.reverse() - does not sort backward alphabetically; it simply
# reverses the order of the list in completely opposite way from the original.
# reverse will be permanent. to revert it back to the original, do 'reverse()' again
# not to confuse w (reverse=true) parameter: list_name.sort(reverse=True) OR sorted(list_name, reverse=True)
print("# reversing the list with reverse() ---------------------")
nums2 = [3, 5, 1, 0, -55, 100]
print(f'original list : {nums2}')
nums2.reverse()
print(f'reversed list : {nums2}')
# so it just reverses the list upside down

# types of errors:
# IndentationError (space), SyntaxError (use square brackets vs parenthesis etc. ),
# TypeError: (concat string + integer),
# NameError: using something (some name) that we have not defined yet
# IndexError: list index out of range (if you only have 5 elements, you can not access 6 or 7)

# H/W: DO THE EXERCISE 3-8 (sorting) -----------------------------
my_places = ['England', 'Australia', 'UAE', 'Portugal', 'Japan']
print(my_places)
print(sorted(my_places))
print(my_places)
print(sorted(my_places, reverse=True))
print(my_places)
my_places.reverse() # reverse the order of the elements from the original in the list
print(my_places)
my_places.reverse() # reverse back to the original
print(my_places)
my_places.sort()
print(my_places)
my_places.sort(reverse=True)
print(my_places)
print(my_places)

# use len() to print a message indicating the number of ppl you are inviting to dinner.
print('this is how long the guest list is', len(dinner_list))

# find out what index an element is by its value (name):
print(my_places.index('Portugal'))
