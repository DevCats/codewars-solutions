# Given an integer, square each digit & concatenate squared digits
# eg: 9119 -> 9**2 + 1**2 + 1**2 + 9**2 -> 81 + 1 + 1 + 81 = 811181

# Use list comprehension to:
    # Cast integer to string
    # Cast each string digit to an integer, square it, then cast it back to a string
# Join new list, cast to an integer & return 

def concat_squared_digits(num):
    sqr_digits = [str(int(digit)**2) for digit in str(num)]
    return int("".join(sqr_digits))