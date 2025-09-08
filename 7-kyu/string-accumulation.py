# Given a string, return a string with:
    # each character repeated a number of times equal to its position in the string
    # new sets of repeated chars separated by hyphens
    # the first char in each set capitalised
# eg: "abcd" -> "A-Bb-Ccc-Dddd"
# eg: "RqaEzty" -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# e.g: "cwAt" -> "C-Ww-Aaa-Tttt"

# Capitalise string
# Convert string to list of chars
# Iterate over sequence equal to length of list
    # Use current index (i) to get char & convert to lowercase
    # Iterate over sequence starting at 1 up to current index (1) plus 1
        # Use index (i) to concatenate list item at index i and current_char variable
# Join modified list using "-" as a separator
# Return

def accum(str):
    str = list(str.upper())
    for i in range(len(str)):
        current_char = str[i].lower()
        for j in range(1, i+1):
            str[i] += current_char
    str = "-".join(str)
    return str