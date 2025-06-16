def postfix_to_infix(expression):
    stack = []
    operators = set(["+", "-", "*", "/"])

    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({operand1} {token} {operand2})"
            stack.append(new_expr)
        else:
            stack.append(token)

    return stack[0]

# Example usage:
n=input().split()
print(postfix_to_infix(n))  # Output: (2 + (3 * 4))