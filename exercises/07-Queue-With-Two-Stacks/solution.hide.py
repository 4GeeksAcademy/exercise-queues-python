class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def enqueue(self, value):
        self.in_stack.append(value)
        return True

    def dequeue(self):
        self._shift()
        if not self.out_stack:
            return None
        return self.out_stack.pop()

    def peek(self):
        self._shift()
        if not self.out_stack:
            return None
        return self.out_stack[-1]


queue = QueueWithStacks()
results = [
    queue.enqueue(5),
    queue.enqueue(6),
    queue.dequeue(),
    queue.peek(),
    queue.dequeue(),
    queue.dequeue(),
]
