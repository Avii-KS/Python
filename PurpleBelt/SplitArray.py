def split_array(arr, x):
    greater = [num for num in arr if num > x]
    lesser_or_equal = [num for num in arr if num <= x]
    return greater, lesser_or_equal

# Input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Processing
greater, lesser_or_equal = split_array(arr, x)

# Output
print(" ".join(map(str, greater)))
print(" ".join(map(str, lesser_or_equal)))
