# today's activity

# Input the temperature in degrees Celsius and convert to Fahrenheit:
# ℉=(9/5)℃+32

c_deg = float(input("Enter Celsius: "))
f_deg = (9 / 5) * c_deg + 32
print(f'{c_deg:.2f}\u00B0 Celsius is {f_deg:.2f}\u00B0 Fahrenheit.')
print()

# Input the temperature in degrees Fahrenheit and convert to Celsius:
# ℃=(5/9)(℉ −32)
f2_deg = float(input("Enter Fahrenheit: "))
c2_deg = (5 / 9) * (f2_deg - 32)
print(f'{f2_deg:.2f}\u00B0 Fahrenheit is {c2_deg:.2f}\u00B0 Celsius.')
print()

# Calculate Body Surface Area (BSA), which is a measure of the skin's
# total area and can be used to determine the calculation of drug
# dosages and the amount of fluids to be administered via IV.
# Input both height and weight before calculating.

# BSA = the square root of (height(cm) x weight(kg)) / 3600

# Math methods: https://docs.python.org/3/library/math.html 

import math

height = float(input("Enter height in cm: "))
weight = float(input("Enter weight in kg: "))
BSA = math.sqrt((height * weight) / 3600)
print(f"For height {height:.1f} cm and weight {weight:.1f} kg, BSA is {BSA:.1f}")
print()

# Input height and radius and calculate the area of a right circular cone (a cone)

# Area = pi * radius * (radius + square root of (h^2 + r^2))

h = float(input("Input height of circular cone: "))
r = float(input("Input radius of circular cone: "))

A = math.pi * r * (r + math.sqrt(h**2 + r**2))
print(f'With height {h:.1f} and radius {r:.1f}, area of cone is {A:.1f}')


