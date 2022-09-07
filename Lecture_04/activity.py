# 2.8 Python example: Salary calculation

# The following program calculates yearly and monthly
# salary given an hourly wage.
# The program assumes a work-hours-per-week of 40
# and work-weeks-per-year of 50. 

# Insert the correct number in the code to print a
# monthly salary.  Then run the program. The monthly salary
# should be 3333.333... . 

# Then modify the code to let users enter their own salary for the calculation.
# Finally, modify the code so the salaries are printed with two digits after the decimal.

hourly_wage = 20

print('Annual salary is: ')
print(hourly_wage * 40 * 50)
print()

print('Monthly salary is: ')
print(((hourly_wage * 40 * 50) / 1))
print()
