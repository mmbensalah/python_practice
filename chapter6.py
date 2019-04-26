# A year is a leap year if it is divisible by 4, unless it is the first year of a century and it is not divisible by 400.
#
# For example:
#
# 1956 is a leap year because 1956 is divisible by 4.
# 1957 is not a leap year, because it is not divisible by 4.
# 1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is the first year of a century and 1900 is not divisible by 400.
# 1600 is a leap year, because 1600 is divisible by 4 and 1600 (although it is the first year of a century) is divisible by 400
# Write a function is_leap that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
def is_leap(year):
    if year % 10  == 0 and year % 400 == 0:
        return True
    elif year % 10 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# assert is_leap(1944) == True
# assert is_leap(2011) == False
# assert is_leap(1986) == False
