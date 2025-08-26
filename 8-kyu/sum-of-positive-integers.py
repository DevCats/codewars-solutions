# Given a list of integers, return the sum of all the positives

# Declare variable to hold the sum value
# Iterate over list
# If number > 0, add it to the sum
# Return sum

def positive_sum(list):
    sum = 0
    for num in list:
        if num > 0:
            sum += num
    return sum
