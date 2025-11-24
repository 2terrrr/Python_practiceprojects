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


# 2 operations
def simple_op(num1, num2, operation):
    """Helper function to perform one operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return None # Will handle error in main function
        return num1 / num2
    return 0

def calculator2(num1, op1, num2, op2, num3):
    """
    Calculates a chain of 2 operations: num1 op1 num2 op2 num3
    Example: 20 + 10 - 5
    Strictly Left-to-Right (No PEMDAS).
    """
    
    # Check for bad inputs first
    if (op1 == '/' and num2 == 0) or (op2 == '/' and num3 == 0):
        return "Error! Division by zero."

    # STRICT Left-to-Right Logic (No PEMDAS):
    # We always perform the first operation (num1 op1 num2) first.
    # Then we use that result with the third number.
    # Example: 10 + 2 * 5. 
    # Step 1: 10 + 2 = 12
    # Step 2: 12 * 5 = 60
    
    intermediate_result = simple_op(num1, num2, op1)
    final_result = simple_op(intermediate_result, num3, op2)
    return final_result

# --- Tests ---

# 1. Left to Right (Addition then Subtraction)
# 20 + 10 = 30, then 30 - 10 = 20
print(f"20 + 10 - 10 = {calculator2(20, '+', 10, '-', 10)}")

# 2. Strict Left to Right (No PEMDAS)
# 10 + 2 = 12, then 12 * 5 = 60
print(f"10 + 2 * 5   = {calculator2(10, '+', 2, '*', 5)}")

# 3. Left to Right (Multiplication then Addition)
# 10 * 2 = 20, then 20 + 5 = 25
print(f"10 * 2 + 5   = {calculator2(10, '*', 2, '+', 5)}")
