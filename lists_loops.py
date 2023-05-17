# Chapter 4 Looping: Iterative actions
# for var_name in list_name:
# for - is loop
# var_names - is a new var you created inside the loop. it's defined only inside the for loop.

# for each loop
magicians = ['alice', 'carolina', 'david']
for magician in magicians: # this means "for each element in the list"
    print(f'magician: {magician}')
    print(magician, '__________')
    print('hello**')
    # if you want to repeat some action for one certain element inside the loop,
    # you should create another for loop inside the for loop
    # for a in x:
        # print(a)

# print(abc)  # out of scope, abc should be used only inside the loop not outside
# print('byeee')

# RANGE -------------------------------------------------------------
# range(startingNumber, endingNumber, steps) - ending number not included.
# NOTE: range does not return a list, you need to use list() functions
# to see the result in a list

# range(10, 20, 2) -> 10, 12, 14, 16, 18
# range(5) -> range(0, 5, 1) -> 0, 1, 2, 3, 4
# range(16, 21) -> range(16, 21, 1) -> 16, 17, 18, 19, 20

# print(f'range : {list(range(5))}')

print(f'range: {list(range(5))}')
print(f'# # using range in a loop -----------------------')

# # Exercise : create a list of squares of numbers from 101 to 110 (inclusive)
print(f'exercise---------')

square_list = [] # this has 0 elements
# when you need create a list out of unknown data, you need to create empty list, and then append it
for num in range(101, 111):
    result = num ** 2 # **2 is a default for calculating square. could also use num*num here
    print(f'square = {result}')
    square_list.append(result) # then, at the end of loop you append the results to that list
# so the number of elements in this list will be equal to the amount of numbers between
# 101(included) and 111(not included). so from 101 to 110 both included.

y = len(square_list) # shows how many elements now in the list
print('the list has',y, 'elements')
print(square_list)

# list comprehension: another way of making that list with squares:
square_list_2 = [value**2 for value in range(101,111)] # here u have to put value**2 before defining value
for value in square_list_2:
    print('2nd option',value)

# find the sum of numbers from 55 to 95 (inclusive)
# phsuedocode - steps in words not in syntax
total = 0
for variable in range(55, 96):
    total = total + variable

# total = total + num  # total += num
# total -= num  # total = total - num
# total *= num  # total = total * num

# SLICING THE LIST (accessing only certain part of the list within range)
# lists with both string and integer elements can be sliced
print("# Slicing in the list: ---------------------------")
nums = [4, 23, 6, 0, -11, 4567, 1234]
print(nums[2:5])  # this includes indexes 2, 3, 4 (5 not included)
print(nums[2:])  # this includes all indexes starting from index 2
print(nums[:5])  # this includes all indexes up to index 5 (not including 5)
print(nums[:])  # this includes all indexes up to index 5 (not including 5)

# Creating a new list out of original list using slice:
nums_2_5 = nums[2:5] # created a new sliced list within a range of elements between 2:5 (5 not incl)
nums_2_end = nums[2:] # created a new sliced list with elements from 2 to end
nums_start_5 = nums[:5] # created a new sliced list from 0 to 5 (5 not included)
nums_copy = nums[:] # created new separate list (object) by copying the original list
nums_copy2 = nums # created reference to the same object (will refer to each other)
print(f"*****nums_copy: {nums_copy}")
print(f"nums_copy2: {nums_copy2}")
print(f"original nums: {nums}")
print("----------------------------------")
nums_copy.append(555) # [:] this appends only this new separate copy
nums.append(666) # this appends both 'nums' and 'nums_copy2' cause they refer to each other
nums_copy2.append(777) # same as nums.append, cause again (nums_copy2=nums) refer to each other
print(f"nums_copy after change: {nums_copy}")
print(f"nums_copy2 after change: {nums_copy2}")
print(f"original nums after change: {nums}")

# example with a string list:
ppp = ['fuzz', 'buzz', 'duzz', 'cuzz', 'muzz']
print('this is sliced', ppp[0:3] ) # prints 0 to 3 ['fuzz', 'buzz', 'duzz']
print('this is sliced', ppp[:3] ) # prints from 0 to 3 (but 3 not included)
print('this is sliced', ppp[3:] ) # prints from 3 (included) until the last element
print('this is sliced', ppp[:] ) # prints all elements from the list

# H/W all exercises of chapter 4 (excluding Tuples section)
animals = ['parrot', 'cat', 'dog']
for xx in animals:
    print(f'a {xx} would make a great pet')
print(f'any of these animals would make a great pet!')
print('the first two items of the list are', animals[:2])

my_fav_pizza = ['magrietta', 'cheese', 'anchovies', 'mushroom', 'veggie']
for x in my_fav_pizza:
    print('I like', x, 'pizza')
print(f'I really love all kinds of pizza!')
print(f'The first three items in the list are: {my_fav_pizza[0:3]}')
print(f'Three items from the middle of the list are: {my_fav_pizza[1:4]}')
print(f'The last three items in the list are: {my_fav_pizza[2:]}')
friend_pizzas = my_fav_pizza[:]

my_fav_pizza.append('seafood pizza')
friend_pizzas.append('chicken pizza')

for x in my_fav_pizza:
    print(f'My favorite pizzas are: {x}')

for x in friend_pizzas:
    print(f'My friend’s favorite pizzas are: {x}')

my_foods = ['pizza', 'falafel', 'carrot cake']
for x in my_foods:
    print(x)

# print the smallest or largest number out of list min(list_name) or max(list_name)
nums2 = [4, 8, 96, 1, 784, 54, 6]
print(min(nums2)) # prints 1
print(max(nums2)) # prints 784
# min() max() also works with STRING values: will pick the shortest and the longest words
list1 = ['a', 'dog', 'corn', 'forest', 'obstacle']
print(min(list1)) # prints 1
print(max(list1)) # prints 784
print('---------------------')

for x in friend_pizzas[:3]: # this is slicing list in for loop
    print(x)