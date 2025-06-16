class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        dummy = Node()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = Node(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

def create_linked_list(values):
    dummy = Node()
    current = dummy
    for val in values:
        current.next = Node(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" ".join(result))

n1 = int(input())
l1_values = list(map(int, input().split()))
n2 = int(input())
l2_values = list(map(int, input().split()))

l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print_linked_list(result)
