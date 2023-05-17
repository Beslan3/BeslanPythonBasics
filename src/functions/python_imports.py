from datetime import datetime
from time import *
from os import *

now = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.today().strftime('%H:%M:%S')
fntimestamp = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

print(f'current date is : {now}')
sleep(5) # holds the execution for 5 seconds. can change the time
print(f'current time is : {current_time}')

current_dir = path.dirname(path.abspath(__file__))
print(f'current dir : {current_dir}')

print(fntimestamp)
