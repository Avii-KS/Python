n=int(input())
matrix=[]
for i in range(n):
  matrix.append(list(map(int, input().split())))
for i in range(n):
  matrix[i][i], matrix[i][n - 1 - i]= matrix[i][n - 1 - i], matrix[i][i]
  print(*matrix[i])
