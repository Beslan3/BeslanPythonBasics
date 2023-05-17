# h/w: create condition that prints 'Fuzz' if number is dividable by 3,
# and returns 'Buzz' if number is dividable by 5
# and returns 'FuzzBuzz' if the number is dividable by 15


# Sample inputs/outputs:
# num = 3  # output 'Fuzz' -> True/False -> Pass/Fail
# num = 27  # output 'Fuzz' -> Pass/Fail
# num = 10  # output 'Buzz' -> Pass/Fail
# num = 30  # output 'FuzzBuzz' -> Pass/Fail
# num = 45  # output 'FuzzBuzz' -> Pass/Fail
# num = 100  # output 'Buzz' -> Pass/Fail
# num = 0  # output 'Not Valid Entry', for any input less than 3 -> Pass/Fail
# num = 'a'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = ''  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = '\t'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail

# 1. list of numbers
# 2. for loop + if num in nums
# 3. how to find out if a num is divisible by another num: num % 3 == 0
# 4. % returns the remainder after division. example: 21%4 = 1 (21/4 =5.. 5*4 =20.. 21-20 =1
# so if % returns 0, that will mean that a number is divisible by another number


print('*****************************')
nums = [25, 9, 30, 100, 45, 27, 65, 63, 240, 2, 1, ]

for num in nums:
    if num %3 ==0:
        print('Fuzz')
    if num%5 ==0:
        print('Buzz')
    if num%15 ==0:
        print('FuzzBuzz')
    if num < 3:
        print('not a valid entry!')
# --------------------------------------------------------------
number = int(input('enter the number: '))
if number%3 == 0:
    print(f'Fuzz')
if number%5 == 0:
    print(f'Buzz')
if number%15 == 0:
    print(f'FuzzBuzz')
if number<3:
    print(f'not a valid entry!')









