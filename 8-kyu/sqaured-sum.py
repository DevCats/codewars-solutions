# Given a list of integers, square each number and return the sum

# Declare variable to hold sum
# Iterate over list of integers
# Square each integer, add it to sum & return outside loop

def squared_sum(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num**2
    return sum