def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2   
        else:
            print("Invalid operator!")
            return calculator()  

        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

    except ValueError:
        print("Error: Invalid number input!")

    choice = input("Do another calculation? (y/n): ").lower()
    if choice == "y":
        calculator()
    else:
        print("Calculator stopped.")
calculator()

