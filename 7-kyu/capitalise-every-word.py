# Given a string, capitalise the first char in every word in the string and return it

# Use list comprehension to:
    # Split string into list of words
    # Use .upper() on the first char using indexes
    # Use .lower() on the remaining chars using indexes
    # Join list & return 

def capitalise(str):
    new_list = [word[0].upper() + word[1:].lower() for word in str.split(" ")]
    return " ".join(new_list)