# Read the postfix expression
postfix = input().split()  # Example: "19 5 2 * +"

# Stack to hold intermediate prefix expressions
stack = []

# Operators set
operators = {'+', '-', '*', '/'}

# Traverse tokens in postfix expression
for token in postfix:
    if token in operators:
        # Pop two operands
        right = stack.pop()
        left = stack.pop()
        # Combine them into prefix form
        new_expr = f"{token} {left} {right}"
        # Push back the result
        stack.append(new_expr)
    else:
        # Token is a number → push it directly
        stack.append(token)

# Final prefix expression is on top of stack
print(stack[0])
