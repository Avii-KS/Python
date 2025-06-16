def string(s):
    stack = []
    for i in s:
        if i in "{[(":
            stack.append(i)
        else:
            if not stack:
                return False
            if i == ')' and stack[-1] != '(':
                return False
            if i == '}' and stack[-1] != '{':
                return False
            if i == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

s = input()
print(string(s))
