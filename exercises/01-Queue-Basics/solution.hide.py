class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
first_out = queue.dequeue()
