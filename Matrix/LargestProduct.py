# Use print() to print to the console
n = int(input())
a = input()
maxProduct = 0

for i in range(len(a)-n+1):
  product = 1
  for j in range(i, i+n):
    product *= int(a[j])
  if product>maxProduct:
    maxProduct = product

print(maxProduct)
