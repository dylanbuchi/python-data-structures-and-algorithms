class Stack():
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return f'{self.stack[::]}'

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())

    s.push(2)
    s.push(3)
    s.push(4)
    s.pop()

    print(s.peek())
    print(s)
    print(s.is_empty())
