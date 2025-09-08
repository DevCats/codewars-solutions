# Given a string, determine if the string has the same number of x's and o's
# Same number or none = True
# Different number = False

# Compare number using .count()

def x_and_o(str):
    return True if str.lower().count("x") == str.lower().count("o") else False