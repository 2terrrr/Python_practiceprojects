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

def calculator3(num1, op1, num2, op2, num3):
    """
    Calculates a chain of 2 operations: num1 op1 num2 op2 num3
    Example: 20 + 10 - 5
    Uses PEMDAS (Multiplication/Division before Addition/Subtraction).
    """
    
    # Check for bad inputs first
    if (op1 == '/' and num2 == 0) or (op2 == '/' and num3 == 0):
        return "Error! Division by zero."

    # PEMDAS Logic:
    # Check if the second operation has higher precedence than the first.
    # If op2 is * or / AND op1 is + or -, we must do op2 first.
    if (op2 in ['*', '/']) and (op1 in ['+', '-']):
        # Right side first: num2 op2 num3
        intermediate_result = simple_op(num2, num3, op2)
        final_result = simple_op(num1, intermediate_result, op1)
        return final_result
    else:
        # Standard Left-to-Right
        intermediate_result = simple_op(num1, num2, op1)
        final_result = simple_op(intermediate_result, num3, op2)
        return final_result

# --- Tests ---

# 1. Left to Right (Addition then Subtraction)
print(f"20 + 10 - 10 = {calculator3(20, '+', 10, '-', 10)}")

# 2. Order of Operations (Multiplication before Addition)
print(f"10 + 2 * 5   = {calculator3(10, '+', 2, '*', 5)}")

# 3. Left to Right (Multiplication then Addition)
print(f"10 * 2 + 5   = {calculator3(10, '*', 2, '+', 5)}")

print(f"10 + 20 - 7 = {calculator3(10, '+', 20, '-', 7)}")

print(f"30 - 27 * 3 = {calculator3(30, '-', 27, '*', 3)}")

# works now