# Calculator with Loop, Input Validation, and Clean Output

def get_number(prompt):
    """Keep asking until the user enters a valid number"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def format_number(n):
    """Convert float to int if it has no decimal part"""
    return int(n) if n.is_integer() else n

while True:
    # Ask the user for input with validation
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

    # Check for quit option
    if operation.lower() == "q":
        print("Exiting calculator. Goodbye!")
        break

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
        print(f"{format_number(num1)} + {format_number(num2)} = {format_number(result)}")
    elif operation == "-":
        result = num1 - num2
        print(f"{format_number(num1)} - {format_number(num2)} = {format_number(result)}")
    elif operation == "*":
        result = num1 * num2
        print(f"{format_number(num1)} * {format_number(num2)} = {format_number(result)}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{format_number(num1)} / {format_number(num2)} = {format_number(result)}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation! Please enter one of +, -, *, /, or 'q' to quit.")

    print()  # Blank line for readability
