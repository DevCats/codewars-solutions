# Given a non-empty string, return the middle char
# If string's length is odd, return middle char
# If string's length is even, return middle 2 chars

# First middle char at index length/2 rounded down (middle char for odd length, 2nd char for even length)
# Second middle char at index length/2 rounded down minus 1 (1st char for even length)

def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else "".join((s[len(s)// 2 -1], s[len(s)// 2]))
