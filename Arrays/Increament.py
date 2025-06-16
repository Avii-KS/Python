n = int(input())
l= list(map(str, input().split()))
r = 0
for i in l:
    if i == "++X" or i=="X++":
        r+= 1
    elif i == "--X" or i=="X--":
        i-=1
print(r)