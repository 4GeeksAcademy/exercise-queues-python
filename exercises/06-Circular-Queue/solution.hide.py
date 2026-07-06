class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            return False
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.head]


cq = CircularQueue(3)
scenario = [
    cq.enqueue(1),
    cq.enqueue(2),
    cq.enqueue(3),
    cq.enqueue(4),
    cq.dequeue(),
    cq.enqueue(4),
    cq.peek(),
]
