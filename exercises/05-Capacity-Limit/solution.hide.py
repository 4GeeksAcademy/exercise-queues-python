class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def enqueue(self, value):
        if self.is_full():
            return False
        self.items.append(value)
        return True

    def is_full(self):
        return len(self.items) >= self.capacity


queue = Queue(2)
enqueue_results = [queue.enqueue(10), queue.enqueue(20), queue.enqueue(30)]
