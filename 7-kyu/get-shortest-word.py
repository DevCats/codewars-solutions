# Given a string, find the length of the shortest word(s)

# Use list comprehension to get a list of word lengths
# Return min(list)

def get_shortest_length(str):
    return min([len(word) for word in str.split(" ")])