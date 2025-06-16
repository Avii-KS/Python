def RemoveSpace(s):
    start=0
    end=len(s)-1
    while start<=end and s[start]==" ":
        start+=1
    while end>=start and s[end]==" ":
        end-=1
    return s[start:end+1]

s=input()
print(RemoveSpace(s))
