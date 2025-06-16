# Read input
n = int(input())  # Read the size of the array
arr = list(map(int, input().split()))  # Read space-separated integers as a list

# Copy the array
copied_arr = arr[:]  # Simple way to copy a list

# Print the copied array
print(*copied_arr)  # Unpacking the list to print elements space-separated
