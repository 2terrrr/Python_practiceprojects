def calculator(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
      num1: The first number.
      num2: The second number.
      operation: The operation to perform (+, -, *, /).

    Returns:
      The result of the operation, or an error message.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation"

# Examples of using the calculator
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")