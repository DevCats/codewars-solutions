# Given a positive integer, return sum of every number from 1 up to, and including, that integer

# Declare variable to hold the sum value
# Iterate over range covering 1 to num+1 (+1 b/c starting from 1, not 0)
# Add each item in range to sum
# Return sum

def summation(num):
    sum = 0
    for digit in range(1, num+1):
        sum += digit
    return sum