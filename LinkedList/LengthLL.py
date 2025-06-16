class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

def length(head):

  if head is None:
    return 0
  
  return 1 + length(head.next)

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

print(length(head))