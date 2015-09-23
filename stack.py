

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)

    assert s.peek() == 2
    assert s.pop() == 2
    assert s.peek() == 1


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


test_stack()



