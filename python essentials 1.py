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
            
print("Here is your sorted list: ", my_list)'''  