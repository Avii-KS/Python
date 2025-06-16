def generateSubsequences(s, index, current, result):
    if index == len(s):  # Base case: end of the string
        if current:  # Avoid adding empty string
            result.append(current)
        return

    # Include current character
    generateSubsequences(s, index + 1, current + s[index], result)

    # Exclude current character
    generateSubsequences(s, index + 1, current, result)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def findSubsequences(s):
    result = []
    generateSubsequences(s, 0, "", result)
    # Sort using custom Bubble Sort instead of .sort()
    bubbleSort(result)
    # Print the sorted subsequences
    for sub in result:
        print(sub)

# Example usage
s = "abc"
findSubsequences(s)
