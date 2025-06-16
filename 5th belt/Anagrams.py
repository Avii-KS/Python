def are_anagrams(string1, string2):
    # If lengths are not equal, they cannot be anagrams
    if len(string1) != len(string2):
        return "Not Anagrams"
    
    # Count characters in both strings
    count1 = {}
    count2 = {}
    for char in string1:
        count1[char] = count1.get(char, 0) + 1
    for char in string2:
        count2[char] = count2.get(char, 0) + 1
    
    # Compare character counts
    return "Anagrams" if count1 == count2 else "Not Anagrams"

# Input
string1, string2 = input().strip().lower().split()

# Output
print(are_anagrams(string1, string2))