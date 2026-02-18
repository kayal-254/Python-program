try:
    # Get user input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform division
    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Division completed successfully")

finally:

    print("Program finished")           