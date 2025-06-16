def print_subarrays(array):
    n = len(array)
    for start in range(n):
        for end in range(start, n):
            subarray = array[start:end + 1]
            print(*subarray)

n = int(input())
array = list(map(int, input().split()))

print_subarrays(array)