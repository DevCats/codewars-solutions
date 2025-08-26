# Given an integer representing the year (YYYY), return the equivalent century (CC)
# 1st century spans from 1 to 100 (inc)
# 2nd century spans from 101 to 200 (inc)
# etc

# Subtract 1 from the given year
# Divide by 100, rounding down
# Add 1 & return

def get_century(year):
    return (year - 1) // 100 + 1