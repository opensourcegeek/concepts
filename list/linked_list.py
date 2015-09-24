from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
        self.size += 1

    def search(self, item):
        current = self.head
        found = False

        if current is None:
            return found

        while current is not None and not found:
            data = current.getData()
            if data == item:
                found = True
                break
            current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        found = False

        if current is None:
            return found

        previous = None

        while current is not None and not found:
            data = current.getData()
            if data == item:
                found = True
                break

            previous == current
            current = current.getNext()

        if found:
            if previous == None:
                self.head = current.getNext()

            else:
                previous.setNext(current.getNext())
            self.size -= 1


def test_fn():
    ml = LinkedList()
    ml.addNode(1)
    ml.addNode(2)
    ml.addNode(3)

    print(ml.search(3))
    assert True == ml.search(3)

    assert True == ml.search(2)

    assert True == ml.search(1)

    assert ml.size == 3

    ml.remove(3)

    assert ml.size == 2
    assert False == ml.search(3)


test_fn()





