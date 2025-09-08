# Given a string, determine if it is an isogram (a word with no repeating letters, consecutive or non-consecutive)
# Upper/lower-case variants of the same character are not considered unique

# Declare empty list
# Loop through chars in lowrcase string
# Check if char not in list
    # If not in list, add to list
    # If in list, clear list & return False - not an isogram 
# Return True outside loop

def is_isogram(str):
    chars = []
    for char in str.lower():
        if char not in chars:
            chars.append(char)
        else:
            chars.clear()
            return False
    return True
        
