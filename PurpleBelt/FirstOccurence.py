def RemoveFirstOccurence(text,word):
    n=len(text)
    m=len(word)
    result=""
    for i in range(n-m+1):
        if text[i:i+m]==word:
            result= text[:i]+text[i+m:]
            break
    return result
    
text=input()
word=input()
print(RemoveFirstOccurence(text,word))
