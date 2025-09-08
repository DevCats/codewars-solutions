#Given a list of non-negative integers and strings, return a new list with the strings filtered out

# Use list comprehension to:
    # Create a new list with items that return True when isinstance(i, int) is called on them
# Return new list

def filter_list(l):
    filtered = [i for i in l if isinstance(i, int)]
    return filtered