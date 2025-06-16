# Read input
postfix = input().split()  # e.g., "2 3 4 * +"

# Stack to hold partial expressions
stack = []

# Set of valid operators
operators = {'+', '-', '*', '/'}

# Go through each token in the postfix expression
for token in postfix:
    if token in operators:
        # Pop two operands from stack
        b = stack.pop()
        a = stack.pop()
        # Create a new infix expression with parentheses
        expr = f"({a} {token} {b})"
        stack.append(expr)  # Push back the expression
    else:
        # It's a number, push directly
        stack.append(token)

# Final result is at the top of the stack
print(stack[0])
