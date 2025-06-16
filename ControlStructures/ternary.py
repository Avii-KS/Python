'''Write a program that takes a single integer as input and determines if it is divisible by 10 using a ternary operator.
Example:
Input:
50

Output:
Yes

Explanation:
- If the number is divisible by 10, the output should be "Yes".
- Otherwise, the output should be "No".
'''
n=int(input())
result="yes" if n%10==0 else "no"
print(result)