'''
Chef works in a kitchen with a flexible schedule. The kitchen operates on a 12-hour clock, and Chef's working hours are from X pm to Y pm (1 ≤ X < Y ≤ 12).
Write a program to determine the number of hours Chef works during a day.
Input:
The input consists of two integers, X and Y, representing Chef's starting and ending working hours respectively.
2 7 (starts at 2pm and ends at 7pm)
Output:
Print the number of hours Chef works during a day.
Example:
Input:
10 11

Output:
1
'''
# Input reading
X, Y = map(int, input().split())

# Calculate the number of hours Chef works
hours_worked =abs (Y - X)

# Output the result
print(hours_worked)
