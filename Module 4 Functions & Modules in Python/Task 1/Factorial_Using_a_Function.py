def factorial(number):
    """Calculate the factorial of a given number using recursion."""
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Call the function with a sample number and print the output
sample_number = 5
print(f"The factorial of {sample_number} is {factorial(sample_number)}")