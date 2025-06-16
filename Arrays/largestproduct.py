n=int(input())
numbers=input()
count=1
products=[]
for i in range(len(numbers)-n):
  for j in range(n):
    count*=int(numbers[i+j])
  products.append(count)
  count=1
print(max(products))
