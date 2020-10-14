class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f'{self.queue[::]}'

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    q = Queue()
    print(q.size())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)

    print(q.peek())
    q.dequeue()
    print(q)
