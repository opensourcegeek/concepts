
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []


class Pole(Stack):
    def __init__(self):
        Stack.__init__(self)

    def push(self, item):
        print(item)
        print(self.peek())
        if self.peek() is None or self.peek() > item:
            self.items.append(item)

        else:
            raise Exception('SizeConstraintViolation')


def test_fn():
    src_pole = Pole()
    src_pole.push(3)
    src_pole.push(2)
    src_pole.push(1)

    dest_pole = Pole()
    helper_pole = Pole()

    num_discs = src_pole.size()

    final_poles = fn(src_pole, dest_pole, helper_pole, num_discs)
    assert final_poles[0].size() == 0 # source pole
    assert final_poles[1].size() == 3 # destination pole
    assert final_poles[2].size() == 0 # helper pole


def fn(src, dest, helper, num_discs):
    print("Started")
    while dest.size() < num_discs:
        dest_top = dest.peek()
        src_top = src.peek()
        helper_top = helper.peek()

        if src_top > dest_top:
            dest.push(src.pop())

        elif src_top > helper_top:
            helper.push(src.pop())

        elif dest_top > helper_top:
            helper.push(dest.pop())

        elif dest_top > src_top:
            src.push(dest.pop())

        elif helper_top > src_top:
            src.push(helper.pop())

        elif helper_top > dest_top:
            dest.push(helper.pop())




test_fn()

