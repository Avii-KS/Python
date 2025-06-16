def canPlaceFlowers(flowerbed, n):
    count = 0
    size = len(flowerbed)
    
    for i in range(size):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
    return False

# Input
size = int(input())
n = int(input())
flowerbed = list(map(int, input().split()))

# Output
print(canPlaceFlowers(flowerbed, n))