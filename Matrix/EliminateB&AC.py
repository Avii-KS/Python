arr = list(input())
s = ""
i = 0
while i < len(arr):
    if arr[i] == 'b':
        i += 1
    elif i + 1 < len(arr) and arr[i] == 'a' and arr[i + 1] == 'c':
        i += 2
    else:
        s += arr[i]
        i += 1
print(s)
