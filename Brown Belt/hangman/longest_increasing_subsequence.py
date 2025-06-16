# Python program to find lis using recursion
# in Exponential Time and Linear Space
def lisEndingAtIdx(arr, idx):
    # Base case
    if idx == 0:
        return 1

    # Consider all elements on the left of i,
    # recursively compute LISs ending with
    # them and consider the largest
    mx = 1
    for prev in range(idx):
        if arr[prev] < arr[idx]:
            mx = max(mx, lisEndingAtIdx(arr, prev) + 1)
    return mx


def lis(arr):
    n = len(arr)
    res = 1
    for idx in range(1, n):
        res = max(res, lisEndingAtIdx(arr, idx))
    return res

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(lis(arr))