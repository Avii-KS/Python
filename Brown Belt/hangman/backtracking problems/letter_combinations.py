def letter_combinations(digits):
    result = []
    num_to_letter_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    def backtrack(i, currString):
        #base case
        if len(currString) == len(digits):
            result.append(currString[:])
            return
        #recursive case
        for c in num_to_letter_map[digits[i]]:
            backtrack(i+1, currString+c)

    backtrack(0, "")
    return result

digits = input()
print(letter_combinations(digits))