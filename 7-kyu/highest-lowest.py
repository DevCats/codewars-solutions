# Given a string of space-separated numbers, return the highest and lowest values

# Use list comprehension to:
    # Split each digit in the string into a list
    # Cast each digit in the new list to an integer
# Use max() & min() to get the highest/lowest value, format a string & return

def high_and_low(number_string):
    # Convert number_string into list of integers
    num_list = [int(num) for num in number_string.split(" ")]
    return f"Highest: {max(num_list)} Lowest: {min(num_list)}"