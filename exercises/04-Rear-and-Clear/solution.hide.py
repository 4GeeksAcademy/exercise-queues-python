class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def rear(self):
        if not self.items:
            return None
        return self.items[-1]

    def clear(self):
        self.items.clear()

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
last_item = queue.rear()
queue.clear()
size_after_clear = queue.size()
