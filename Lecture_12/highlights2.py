# Create a list of recorded high temperatures for a week.
# Find the minimum and maximum high temperatures.
# Find the average high temperature.
# Find the median high temperature (using material from future lectures).

# What would need to be different for a list of low temperatures?

high_temps = [70, 60, 65, 55, 68, 72, 71]

# sun_high = 50
# mon_high = 60
# tue_high = 65

print(high_temps)
print("The lowest high was", min(high_temps))
print("The highest high was", max(high_temps))
print("Average high was", sum(high_temps) / len(high_temps))
print("Sunday's high:", high_temps[0])
print("Friday's high:", high_temps[5])
