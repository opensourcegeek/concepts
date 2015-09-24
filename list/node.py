
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getData(self):
        return self.data



