# Given an integer, determine whether it is a square number

# Check if n is greater than or equal to 0
# If it is:
    # Calculate square root of n & cast to integer
    # Check if square root of n multiplied by itself is equal to n & return bool
# Else return False

def is_square(n):
    if n >= 0:
        sq_root = int(n ** 0.5)
        return (sq_root * sq_root == n)
    else:
        return False
