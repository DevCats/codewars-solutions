# Given a string, remove the first and last chars

# Check if string length less than/equal to 2
# If true, return empty string
# Else, remove first and last chars & return

def remove_chars(s):
    return "" if len(s) <= 2 else s[1:-1]