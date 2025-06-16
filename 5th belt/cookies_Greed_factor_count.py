def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def findContentChildren(g, s):
    bubble_sort(g)
    bubble_sort(s)
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child

n = int(input())
g = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))
print(findContentChildren(g, s))