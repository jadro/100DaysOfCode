# Udemy course 100 days of code, day 2

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_qty = int(input("How many people to split the bill? "))

result = (bill + (bill * (percentage / 100))) /people_qty

print("Each person should pay: ${:2f}".format(result))