class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


empty_queue = Queue()
result_on_empty = empty_queue.dequeue()
