# an immutable list is called a TUPLE
# immutable = values that cannot change
#
# The same nature as list, but with parenthesis (not square brackets)
# immutable: in Tuples elements can not be updated, elements can not be deleted
# lists are mutable data structure, tuples are immutable data structure.


coordinatesList = [456, 3455]
coordinatesTuple = (456, 6577)
coordinatesList.append(7895)
print(coordinatesList)
print('List : coordinatesL[0]: ', coordinatesList[0])
print('Tuple : coordinatesT[0]: ',coordinatesTuple[0])
coordinatesList[0] = 789

# you can assign a whole new value to the variable of the tuple, but not change individual items.
coordinatesTuple = (3434234342)
print(coordinatesTuple)


# Exercises:

five_basic_foods = ('chicken', 'mac & cheese', 'soup', 'fries', 'desert')
for x in five_basic_foods:
    print(x)

five_basic_foods = ('beef', 'rice', 'veggie soup', 'fries', 'chocolate')
for x in five_basic_foods:
    print('----',x)