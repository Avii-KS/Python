def generate_parentheses(n, open, close, s, ans):
    #base case
    if open == n and close == n:
        ans.append(s)
        return
    # At any index i in the generation of the string s,
    # we can put an open parentheses only if its count
    # until that time is less than n.
    if open < n:
        generate_parentheses(n, open + 1, close, s + "(", ans)

    # At any index i in the generation of the string s,
    # we can put a closed parentheses only if its count until
    # that time is less than the count of open parentheses.
    if close < open:
        generate_parentheses(n, open, close + 1, s + ")", ans)

def AllParenthesis(n):
    # List for storing the answer
    ans = []
    if n > 0:
        generate_parentheses(n, 0, 0, "", ans)
    return ans


n = 3
ans = AllParenthesis(n)

for s in ans:
    print(s)
