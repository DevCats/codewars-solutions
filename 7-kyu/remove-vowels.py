# Given a string, remove all vowels

# Iterate over each char in string
# Check if char in string of upper/lower-case vowels
# If true, replace char in string with empty string
# Return outside of string

def remove_vowels(string):
    for char in string:
        if char in "aeiouAEIOU":
            string = string.replace(char, "")
    return string