n = int(input())  
nums = list(map(int, input().split()))  
n_value = int(input())  
result = []
for i in range(n_value):
    result.append(nums[i])        
    result.append(nums[n_value + i])
print(*result)

