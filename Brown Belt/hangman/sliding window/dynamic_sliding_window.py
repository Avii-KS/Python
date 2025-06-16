#to find the minimum number of continuous digits who's sum is greater than or equal to x
def dynamic_sliding_window(arr, x):
    #track min value
    min_length=float('inf')
    start = 0
    end = 0
    curr_sum = 0

    #extend the sliding window until the criteria is met
    while end < len(arr):
        curr_sum += arr[end]
        end +=1

        #Contract the sliding window until it no longer meets the condition
        while start < end and curr_sum>=x:
            curr_sum -= arr[start]
            start +=1
            min_length = min(min_length, end-start+1)

    return min_length
arr = [1, 2, 3, 4, 5, 6]
x = 7
print(dynamic_sliding_window(arr, x))
#time complexity is O(N)