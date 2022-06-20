'''secret_number = 777

guess = int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Guess again: "))
    
print(guess, "Well done, muggle! You are free now.")


# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.
# Note: the height is measured by the number of fully completed layers.

blocks = int(input("Enter the number of blocks: "))
height = 0

while blocks > height + 1:
    height += 1
    blocks = blocks - height

print("The height of the pyramid:", height)


# Write a program which reads one natural number and executes the above steps(take any non-negative and non-zero 
# integer number and name it c0; if it is even, evaluate a new c0 as c0 / 2,
# otherwise, if it is odd, evaluate a new c0 as 3 * c0 + 1) as long as c0 remains different 
# from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the 
# intermediate values of c0, too.


c0 = int(input("Enter a number greater than 0: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        steps += 1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
        steps += 1
print("steps: ", steps)

# Sorting lists - slow 

my_list = []  # list to sort
swapped = True  #watches to see is any swaps occurred
num = int(input("How many numbers do you want to add?  "))

for i in range(num):
    list_num = int(input("Enter a number to add to the list  "))
    my_list.append(list_num)
    
print("Here is your list: ", my_list)

my_list.sort()
            
print("Here is your sorted list: ", my_list)


#creates 2 dimension array consisting of 8 rowas and 8 columns with 64 EMPTY spaces

board = [[EMPTY for i in range(8)] for j in range (8)]]

 #creates a 3 dimensional array for 3 buildings with 15 floors and 20 "not occupied" rooms each
 
 rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e) 

t = [[3 - i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s+= t[i][i]
print(s)  

for i in range(1):
    print("#")
else:
    print("#") 
    
# Functions

def message(number):
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

print(a + b + c)
    
def hello(name):
    print("Howdy", name)
    
name = input("What is your name?  ")

hello(name)

def introduction(first_name, last_name):
    print("Hi, my name is", first_name, last_name)

introduction("Critters", "Stafford")
introduction("Eleven", "Hopper")
introduction("Ada", "Lovelace")


def introduction(f_name, l_name):
    print("Hello, my name is", f_name, l_name)

introduction(f_name = "James", l_name = "Bond")
introduction(l_name = "Skywalker", f_name = "Luke")

def is_year_leap(year):
#
    if (year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False
#

def days_in_month(year, month):

    if month == 2 and is_year_leap(year):
        return 29
    
    elif month == 2 and not is_year_leap(year):
        return 28
        
    elif month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        
    elif month in (4, 6, 9, 11):
        return 30
        
    else:
        return
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	result = days_in_month(yr, mo)
	print(yr, mo, result, "->", end="")
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
  
  
def lb_to_kg(lb):
    kg = round(lb * 0.45359237, 2)
    return kg
    
def feet_to_meters(feet, inches):
    meters = round((feet * 0.3048), 2) + round((inches * 0.0254), 2)
    return meters

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(lb_to_kg(130), feet_to_meters(5, 6)))
print(bmi(58.97, 1.67))

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))
'''
    
    
