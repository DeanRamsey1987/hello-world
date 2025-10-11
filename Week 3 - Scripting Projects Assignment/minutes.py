years = int(input("Enter number of years: "))

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

minutes = years * days_in_year * hours_in_day * minutes_in_hour

print("There are", minutes, "minutes in", years, "years.")

input("Press Enter to exit...")