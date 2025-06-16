def compress_string(s):
    compressed = ""
    count = 1
    
    for i in range(1, len(s)):  
        if s[i] == s[i - 1]:  
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1  

    compressed += s[-1] + str(count)  

    if len(compressed) < len(s):  
        return compressed  
    else:  
        return s  

# Input
s = input()  # Read input directly without strip()

# Output
print(compress_string(s))
