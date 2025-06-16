class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Input processing
q = int(input())
stack = MinStack()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:  # PUSH
        stack.push(query[1])
    elif query[0] == 2:  # POP
        stack.pop()
    elif query[0] == 3:  # Get Minimum Element
        print(stack.getMin())