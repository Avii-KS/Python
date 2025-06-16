n=int(input())
a, b = 0, 1
for i in range(n):
    if a > n:
        break
    print(a, end=' ')
    a, b = b, a + b
