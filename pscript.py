# Week number of the year (d)
week_number_of_year = current_time.isocalendar()[1]
print(f"Week Number of the Year: {week_number_of_year}")

# Week number of the month (e)
# Using the date and isocalendar approach for calculating this
first_day_of_month = current_time.replace(day=1)
week_number_of_month = (current_time - first_day_of_month).days // 7 + 1
print(f"Week Number of the Month: {week_number_of_month}")

# Day of the year (f)
day_of_year = current_time.timetuple().tm_yday
print(f"Day of the Year: {day_of_year}")

# Day of the month (g)
day_of_month = current_time.day
print(f"Day of the Month: {day_of_month}")

# Day of the week (h)
day_of_week = current_time.strftime('%A')  #
