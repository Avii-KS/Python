s = input()
c1 = 0
c2 = 0
c3 = 0

for i in s:
    if i == '0':
        c1 += 1
    elif i == '1':
        c2 += 1
    else:
        c3 += 1

if c1 == c2 == c3:
    print("yes")
else:
    print("no")
