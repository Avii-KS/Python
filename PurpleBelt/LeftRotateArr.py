def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

n, d = map(int, input().split())
arr = list(map(int, input().split()))
left_rotate(arr, d)
print(" ".join(map(str, arr)))
