def lastOccurrence(t,w):
    n=len(t)
    m=len(w)
    r=""
    for i in range(n-m,-1,-1):
        if t[i:i+m]==w:
            r=t[:i]+t[i+m:]
            break
    return r
        
t=input()
w=input()
print(lastOccurrence(t,w))