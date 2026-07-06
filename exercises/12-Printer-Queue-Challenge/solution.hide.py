class PrintQueue:
    def __init__(self):
        self.jobs = []
        self._counter = 0

    def add_job(self, name, pages, priority):
        self.jobs.append((priority, self._counter, name, pages))
        self._counter += 1
        self.jobs.sort(key=lambda item: (item[0], item[1]))

    def next_job(self):
        if not self.jobs:
            return None
        _, _, name, _ = self.jobs.pop(0)
        return name

    def pending_pages(self):
        return sum(job[3] for job in self.jobs)


printer = PrintQueue()
printer.add_job("report", 20, 3)
printer.add_job("invoice", 2, 1)
printer.add_job("slides", 15, 2)
printer.add_job("notes", 4, 1)
processed = [printer.next_job(), printer.next_job(), printer.next_job()]
pages_left = printer.pending_pages()
