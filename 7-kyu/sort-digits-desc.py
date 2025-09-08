# Given any positive integer, sort its digits in descending order & return this value

# Cast num to string
# Use list() to get a list of digits in num
# Use sorted() to sort the list in descending order
# Join the sorted list into a single string
# Cast string to integer & return

def sort_digits_desc(num):
    num_str = str(num)
    num_list = list(num_str)
    desc_num_list = sorted(num_list, reverse=True)
    result = "".join(desc_num_list)
    return int(result)