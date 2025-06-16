def removeKdigits(num: str, k: int) -> str:
    stack = []

    for digit in num:
        # Remove digits from the stack if they are larger than the current digit
        # and we still need to remove more digits (k > 0)
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        # Append the current digit to the stack
        stack.append(digit)

    # Remove remaining digits from the end if k > 0
    stack = stack[:-k] if k > 0 else stack

    # Convert the stack to a number and remove leading zeros
    result = ''.join(stack).lstrip('0')

    # If the result is empty, return "0"
    return result if result else "0"


# Example usage
num = input("Enter the number: ")
k = int(input("Enter the number of digits to remove: "))
print("Smallest number after removal:", removeKdigits(num, k))