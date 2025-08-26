# Given a positive or negative integer, find its inverse number
# i.e if num is positive make it negative, if it's negative make it positive

def inverse_num(num):
    return abs(num) if num < 0 else num * -1