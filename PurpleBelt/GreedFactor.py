def findContentChildren(g, s):
    
    i = j = 0  # Pointers for children and cookies
    count = 0  # Number of satisfied children
    
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:  # If cookie satisfies child's greed
            count += 1
            i += 1  # Move to the next child
        j += 1  # Move to the next cookie
    
    return count

# Example Input
n = int(input())  # Number of children
g = list(map(int, input().split()))  # Greed factors
m = int(input())  # Number of cookies
s = list(map(int, input().split()))  # Cookie sizes

# Output the result
print(findContentChildren(g, s))
