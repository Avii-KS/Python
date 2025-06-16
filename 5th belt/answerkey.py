def maxConsecutiveAnswers(answerKey, k):
    def maxConsecutive(char):
        left, right = 0, 0
        max_length = 0
        changes = 0

        while right < len(answerKey):
            if answerKey[right] != char:
                changes += 1

            while changes > k:
                if answerKey[left] != char:
                    changes -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

    return max(maxConsecutive('T'), maxConsecutive('F'))

# Input
answerKey = input()
k = int(input())

# Output
print(maxConsecutiveAnswers(answerKey, k))