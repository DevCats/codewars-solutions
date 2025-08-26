# Reverse the string passed as an argument

def reverse_str(string):
    # reversed() takes & returns an iterable
    result = "".join(reversed(string))
    return result