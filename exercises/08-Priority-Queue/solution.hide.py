class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value, priority):
        self.items.append((priority, value))
        self.items.sort(key=lambda item: item[0])

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)[1]

    def peek(self):
        if not self.items:
            return None
        return self.items[0][1]


pq = PriorityQueue()
pq.enqueue("low", 5)
pq.enqueue("urgent", 1)
pq.enqueue("normal", 3)
order = [pq.dequeue(), pq.dequeue(), pq.dequeue()]
