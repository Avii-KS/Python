n=int(input())
l=list(map(int,input().split()))
m=max(l)
l.remove(m)
print(max(l))

