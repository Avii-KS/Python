def generateParentheses(n, current="", open_count=0, close_count=0, result=None):
    if result is None:
        result = []

    if len(current) == 2 * n:
        result.append(current)
        return result

    if open_count < n:
        generateParentheses(n, current + "(", open_count + 1, close_count, result)
    if close_count < open_count:
        generateParentheses(n, current + ")", open_count, close_count + 1, result)

    return result

# Taking input from the user
n = int(input().strip())
print(generateParentheses(n))