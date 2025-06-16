n = int(input()) 
l = list(map(int, input().split()))
largest_index = l.index(max(l))
smallest_index = l.index(min(l))
l[largest_index], l[smallest_index] = l[smallest_index], l[largest_index]
print(*l)

