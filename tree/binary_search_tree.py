
def test_fn():
    root = None
    root = insert(root, 20)
    #printNodes(root)
    root = insert(root, 15)
    #printNodes(root)
    root = insert(root, 25)
    root = insert(root, 19)
    root = insert(root, 23)
    printNodes(root)


class BSTNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def printNodes(root):
    if root is None:
        print("Nothing in BST")
        return

    else:
        print("The data is {}".format(root.data))
        if root.left is not None:
            print("Printing left sub-tree")
            printNodes(root.left)


        if root.right is not None:
            print("Printing right sub-tree")
            printNodes(root.right)

        return


def insert(root, item):

    if root is None:
        print("No data block")
        print(item)
        node = BSTNode()
        node.data = item
        root = node
        return root

    elif item > root.data:
        print("Greater than block")
        print(item)
        print(root.data)
        root.right = insert(root.right, item)
        return root

    elif item < root.data:
        print("Lesser than block")
        print(item)
        print(root.data)
        root.left = insert(root.left, item)
        return root


if __name__ == '__main__':
    test_fn()
