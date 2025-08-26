# Given a list of values, return the number of truthy values

# Declare counter variable
# Iterate over list
# If truthy, increase count by 1
# Return count outside of loop

def total_truthy(list):
    count = 0
    for i in list:
        if i:
            count += 1
    return count