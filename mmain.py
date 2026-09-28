def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


while True:
    operation = input("Choose an operation (+, -, *, /) or type 'q' to quit: ")

    if operation.lower() == 'q':
        print("Goodbye!")
        break

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    try:
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
