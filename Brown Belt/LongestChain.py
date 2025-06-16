def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])  # Sort by the second element of each pair
    current_end, count = float('-inf'), 0
    
    for left, right in pairs:
        if left > current_end:
            current_end = right
            count += 1
            
    return count

# Taking input from the user
n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]

print(findLongestChain(pairs))