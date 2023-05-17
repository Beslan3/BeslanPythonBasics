age = 16
age_str = '16'
print('you are eligible at', age + 5)

# CONVERTING DATA TYPES:
print('CONVERTING DATA TYPES -------------')
# you can't concatenate integer with string value like the following:
# print('you are eligible at' + age) - this will give you error
# to get it done you need to CONVERT INTEGER TO STRING like this:
print('you are eligible at ' + str(age) )
# or
print('you are eligible at ' + age_str)
# int() function converts string (text) numbers to an integer:
print('after 10 years you will be', int(age_str) + 10,'!')
# str() function in this case converts integer back to string:
print('after 10 years you will be ' + str(int(age_str) + 10) + '!' )
# using F STRING (more preferred way): easier to control the space and overall your code.
print(f' f string, after 10 years you will be {int(age_str) + 10}!')

# float() - converts integer into float (meaning same number, but with decimals) in the parentheses must be an integer var or a number .
print(f'converting integer to float (decimals): {float(age)}')



