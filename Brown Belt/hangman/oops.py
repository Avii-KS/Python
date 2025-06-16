class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        total = val1 + val2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

def createLinkedList(numbers):
    dummy_head = ListNode(0)
    current = dummy_head
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next

def printLinkedList(l):
    current = l
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Read input
nums1 = list(map(int, input("Enter the first number (digits separated by space, in reverse order): ").split()))
nums2 = list(map(int, input("Enter the second number (digits separated by space, in reverse order): ").split()))

# Create linked lists
l1 = createLinkedList(nums1)
l2 = createLinkedList(nums2)

# Add the two numbers
result = addTwoNumbers(l1, l2)

# Print the result
print("The sum as a linked list is: ", end="")
printLinkedList(result)
