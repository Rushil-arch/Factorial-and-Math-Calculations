# Task 2: Using the Math Module for Calculations

import math

# Ask the user for a number as input
number = float(input("Enter a number: "))

# Calculate the square root, natural logarithm, and sine of the number
sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

# Display the calculated results
print(f"The square root of {number} is: {sqrt_result}")
print(f"The natural logarithm (log base e) of {number} is: {log_result}")
print(f"The sine of {number} (in radians) is: {sine_result}")


