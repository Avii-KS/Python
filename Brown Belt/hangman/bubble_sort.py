def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
array = list(map(int, input().split()))
bubbleSort(array)
print(*array)
