"""Find if a year is a leap year"""
def leap_year(year):
    """main logic is here"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False