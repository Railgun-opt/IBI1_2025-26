# What does this piece of code do?
# Answer: It calculates and prints the sum of 11 randomly generated integers, each between 1 and 10.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil 
# 💡 Note: ceil is imported here, but it is never actually used in the code below!

total_rand = 0  # Variable to track the sum of random numbers, initialized to 0
progress = 0    # Loop counter, initialized to 0

while progress <= 10:  # Loop while progress is less than or equal to 10 (runs 11 times: 0 to 10)
    progress += 1      # Increment the counter by 1 in each iteration
    n = randint(1, 10) # Generate a random integer between 1 and 10 and assign it to n
    total_rand += n    # Add the random number n to the total_rand sum

print(total_rand)      # Print the final sum after the loop finishes