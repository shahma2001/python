import calendar

def is_leap_year(year):
    # Use the calendar module's isleap function to check for leap year
    return calendar.isleap(year)

# Input year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


