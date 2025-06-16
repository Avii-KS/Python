def is_rotated_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_palindrome(rotated):
            return "Yes, the rotated string is a palindrome."
    return "No, no rotation creates a palindrome."

# Example input
s = input()  # Input the string
print(is_rotated_palindrome(s))