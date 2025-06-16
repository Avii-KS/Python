#Leetcode question 3: Longest substring without repeating characters

def lengthOfLongestSubstring(s):
    l = 0
    longest = 0
    char_set = set()
    n = len(s)

    for r in range(n):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        longest = max(longest, r - l + 1)

    return longest

s = "abb"
print(lengthOfLongestSubstring(s))