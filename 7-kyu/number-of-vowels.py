# Given a string, return the number of vowels

# Declare counter & vowel list variables
# Iterate over each char in string
# If char is in vowel list, increase counter by 1
# Return count outside of loop


def get_vowel_count(string):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in range(len(string)):
        if string[char] in vowels:
            count += 1
    return count