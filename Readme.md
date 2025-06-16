<!-- def string(s):
stack = []
for i in s:
if i in "{[(":
stack.append(i)
else:
if not stack:
return False
if i == ')' and stack[-1] != '(':
return False
if i == '}' and stack[-1] != '{':
return False
if i == ']' and stack[-1] != '[':
return False
stack.pop()
return len(stack) == 0

s = input()
print(string(s))

def toggle(s):
r=""
for i in s:
if i.isupper():
r+=i.lower()
else:
r+=i.upper()
return r

s=input()
print(toggle(s))

def suffixSum(arr):
r=sum(arr)
ss=[]
for i in range(len(arr)):
s= r-sum(arr[:i])
ss.append(s)
return ss

n=int(input())
arr=list(map(int,input().split()))
print(\*suffixSum(arr))

def SeperateEandO(arr):
r1 = []
r2 = []
for i in arr:
if i % 2 == 0:
r1.append(i)
else:
r2.append(i)
return r1, r2

n=int(input())
arr=list(map(int,input().split()))
even,odd= SeperateEandO(arr)
print(*even)
print(*odd)

def selection_sort(arr):
for i in range(len(arr)):
min_idx = i
for j in range(i + 1, len(arr)):
if arr[min_idx] > arr[j]:
min_idx = j
arr[i], arr[min_idx] = arr[min_idx], arr[i]
return arr

n = int(input())
arr = list(map(int, input().split()))
output = selection_sort(arr)
print(" ".join(map(str, output)))

def SecondLargestEle(arr):
for i in range(n-1):
for j in range(n-1-i):
if arr[j]<arr[j+1]:
arr[j],arr[j+1]=arr[j+1],arr[j]
return arr[1]

n=int(input())
arr=list(map(int,input().split()))
print(SecondLargestEle(arr))

def right_rotate(arr, d):
n = len(arr)
d = d % n
return arr[d:] + arr[:d]
n, d = map(int, input().split())
arr = list(map(int, input().split()))
rotated_arr = right_rotate(arr, d)
print(" ".join(map(str, rotated_arr)))

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

def duplicate(arr):
elem=[]
for i in arr:
if i not in elem:
elem.append(i)
return elem

n=int(input())
arr=list(map(int,input().split()))
print(\*duplicate(arr))

def sortedArray(arr1,arr2):
r=arr1+arr2
for i in range(len(r)):
for j in range(len(r)-i-1):
if r[j]>r[j+1]:
r[j],r[j+1]=r[j+1],r[j]
return r

n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
print(\*sortedArray(arr1,arr2))

def mergeSort(array):
if len(array) > 1:
mid = len(array) // 2
left_half = array[:mid]
right_half = array[mid:]
mergeSort(left_half)
mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

array = list(map(int, input().split()))
print(\*mergeSort(array))

def left_rotate(arr, d):
n = len(arr)
d = d % n
return arr[-d:] + arr[:-d]

n, d = map(int, input().split())
arr = list(map(int, input().split()))
left_rotate(arr, d)
print(" ".join(map(str, arr)))

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

def power(x, n):
if n == 0:
return 1
if n < 0:
return 1 / power(x, -n)
if n % 2 == 0:
half*power = power(x, n // 2)
return half_power * half*power
else:
return x * power(x, n - 1)

x = float(input())
n = int(input())

result = power(x, n)
print(result)

def greaterandlower(arr):
g=[]
l=[]
for i in arr:
if i>m:
g.append(i)
else:
l.append(i)
print(*g)
print(*l)

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
greaterandlower(arr)

def RemoveFirstOccurence(text,word):
n=len(text)
m=len(word)
result=""
for i in range(n-m+1):
if text[i:i+m]==word:
result= text[:i]+text[i+m:]
break
return result

text=input()
word=input()
print(RemoveFirstOccurence(text,word))

s = input()
alphabets = 0
digits = 0
special_char = 0
for i in s:
if i.isalpha():
alphabets += 1
elif i.isdigit():
digits += 1
else:
special_char += 1
print(alphabets, digits, special_char)

# Read input

n = int(input()) # Read the size of the array
arr = list(map(int, input().split())) # Read space-separated integers as a list

# Copy the array

copied_arr = arr[:] # Simple way to copy a list

# Print the copied array

print(\*copied_arr) # Unpacking the list to print elements space-separated

def Sorted(arr):
for i in range(n-1):
if arr[i]>arr[i+1]:
return 0
return 1

n=int(input())
arr=list(map(int,input().split()))
print(Sorted(arr))

def BubbleSort(arr):
for i in range(n+1):
for j in range(n-i-1):
if arr[j]>arr[j+1]:
arr[j],arr[j+1]=arr[j+1],arr[j]
return arr

n=int(input())
arr=list(map(int,input().split()))
print(\*BubbleSort(arr)) -->
