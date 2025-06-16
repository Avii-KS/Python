def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

n = int(input())
arr = list(map(int, input().split()))
output = selection_sort(arr)
print(" ".join(map(str, output)))
