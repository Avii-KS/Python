n=int(input())
s=input()
count1=0
count2=0

for i in range(len(s) - 1):
    if s[i] == "S" and s[i + 1] == "F":
        count1 += 1
    elif s[i] == "F" and s[i + 1] == "S":
        count2 += 1
        
if count1>count2:
    print('Yes')
else:
    print('No')
            