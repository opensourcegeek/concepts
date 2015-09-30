
def test_fn():
    bst = Tree()
    bst.insert(5)
    bst.insert(16)
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    bst.insert(14)
    bst.insert(18)
    bst.insert(15)

    bst.print_in_order()

    print(bst.search(4).data)
    print(bst.search(10))

    print(bst.find_min())

    bst.delete(4)

    bst.delete(5)

    bst.print_in_order()
    print("")
    print("Kth smallest is {}".format(bst.find_kth_smallest(5)))
    print("Kth smallest is {}".format(bst.find_kth_smallest(1)))



class BSTNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.is_left_child = False
        self.is_right_child = False

        self.left = None
        self.right = None

    def insert(self, node):
      if node.data > self.data:
          if self.right is None:
              self.right = node
              self.right.parent = self
              self.right.is_right_child = True

          else:
              self.right.insert(node)

      elif node.data < self.data:
          if self.left is None:
              self.left = node
              self.left.parent = self
              self.left.is_left_child = True

          else:
              self.left.insert(node)

    def search_node(self, node):
        if node.data > self.data:
            if self.right is None:
                return None
            else:
                return self.right.search_node(node)

        elif node.data < self.data:
            if self.left is None:
                return None

            else:
                return self.left.search_node(node)

        else:
            print("Data found")
            return self


    def print_in_order(self):
        # left
        if(self.left is not None):
            self.left.print_in_order()

        # data
        if self.parent is not None:
            print(str(self.data) + " (" + str(self.parent.data) + ")"),

        else:
            print(str(self.data) + " ( Root )"),

        # right
        if (self.right is not None):
            self.right.print_in_order()


    def find_min(self):
        if (self.left is not None):
            return self.left.find_min()

        else:
            return self

    def find_max(self):
        if (self.right is not None):
            return self.right.find_max()

        else:
            return self


    def delete(self, node):
        if node.parent:
            print("Trying to delete data {} - parent {}".format(node.data, node.parent.data))

        else:
            print "No parent found - possibly root needs to be deleted"

        if node.right is None and node.left is None:
            print("Has no children on both sides")

            node.data = None

            if node.parent:
                if node.is_left_child:
                    node.parent.left = None

                else:
                    node.parent.right = None

        elif node.left is None:
            print("Has no left child")
            node.data = None
            if node.parent:
                if node.is_left_child:
                    node.parent.left = node.right
                    node.right.parent = node.parent

                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent

        elif node.right is None:
            print("Has no children on one side")
            node.data = None

            if node.parent:
                if node.is_left_child:
                    node.parent.left = node.left
                    node.left.parent = node.parent

                else:
                    node.parent.right = node.left
                    node.left.parent = node.parent

        else:
            print("Has children")
            # minimum of right sub-tree can replace current node
            min_node = node.right.find_min()
            node.data = min_node.data

            if node.parent:
                if node.is_left_child:
                    node.parent.left = min_node
                    #node.left.parent = min_node.parent

                else:
                    node.parent.right = min_node

            min_node.delete(min_node)

    def find_smallest_at_k(self, k, stack, i):
        if self is None:
            return i

        if (self.left is not None):
            i = self.left.find_smallest_at_k(k, stack, i)

        print(stack, i)
        stack.insert(i, self.data)
        i += 1

        if i == k:
            print(stack[k - 1])
            print "Returning"


        if (self.right is not None):
            i = self.right.find_smallest_at_k(k, stack, i)

        return i



class Tree:
    def __init__(self):
        self.root = None


    def insert(self, item):
        if self.root is None:
            self.root = BSTNode(item)

        else:
            self.root.insert(BSTNode(item))

    def search(self, item):
        search_for = BSTNode(item)
        return self.root.search_node(search_for)


    def delete(self, item):
        node_to_delete = self.search(item)
        print node_to_delete
        if node_to_delete:
            self.root.delete(node_to_delete)

        else:
            raise Exception("cannot find node to delete")

    def find_min(self):
        min_node = self.root.find_min()
        print("Minimum is {}".format(min_node.data))
        return min_node

    def find_max(self):
        max_node = self.root.find_max()
        print("Max is {}".format(max_node.data))
        return max_node


    def print_in_order(self):
        self.root.print_in_order()

    def find_kth_smallest(self, k):
        #our_stack = []
        #self.root.find_smallest_at_k(k, our_stack, 0)

        #print(our_stack)
        #return our_stack[k-1]
        stack = []
        current = self.root

        while (stack != [] or current != None):
            if(current != None):
                stack.append(current)
                current = current.left

            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.data

                print(node)

                current = node.right


        return None



test_fn()
