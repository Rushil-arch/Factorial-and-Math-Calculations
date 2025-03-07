# Task 1: Calculate Factorial Using a Function

# Define the factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number and print the output
sample_number = 5
result = factorial(sample_number)
print(f"The factorial of {sample_number} is: {result}")


