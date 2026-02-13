# Ethan Mayer
# Feb. 10, 2026

def is_leap_year(year):
    """
    Determine if a year is a leap year.
    
    A year is a leap year if:
    - It's divisible by 4 AND not divisible by 100, OR
    - It's divisible by 400
    """
    # Conditional expression: (Condition A AND Condition B) OR Condition C
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Test with birth year and closest leap year
birth_year = 1998  # Example birth year (not a leap year)
closest_leap_year = 2000  # Closest leap year

print(f"Is {birth_year} a leap year? {is_leap_year(birth_year)}")
print(f"Is {closest_leap_year} a leap year? {is_leap_year(closest_leap_year)}")

def isLeapYear(year):
    """
    Determine if a year is a leap year using if-statements.
    
    Returns "Leap year" or "Not a leap year"
    """
    # Check if divisible by 400 first (most specific condition)
    if year % 400 == 0:
        return "Leap year"
    
    # Check if divisible by 100 (century year, not leap year)
    if year % 100 == 0:
        return "Not a leap year"
    
    # Check if divisible by 4 (regular leap year)
    if year % 4 == 0:
        return "Leap year"
    
    # Default: not a leap year
    return "Not a leap year"


# Test with birth year and closest leap year
birth_year = 1998
closest_leap_year = 2000

print(f"{birth_year}: {isLeapYear(birth_year)}")
print(f"{closest_leap_year}: {isLeapYear(closest_leap_year)}")
