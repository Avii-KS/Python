
a,b,c=(map(float,input().split()))
dt= b*b - 4*a*c

if dt==0:
    print("Equal")

elif dt<0:
    print("Complex")
elif dt>0:
    print("Real")
else:
    print("Invalid")