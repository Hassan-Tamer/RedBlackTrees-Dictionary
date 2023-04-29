# 1 red
# 0 black


# node
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # new node always red


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.size = 0

    def insert_node(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        y = None
        x = self.root

        # find position
        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            elif node.data > x.data:
                x = x.right
            else:
                print("Duplicate key")
                return False

        self.size = self.size + 1
        node.parent = y  # parent of node is y
        if y is None:  # only one node
            self.root = node
        elif node.data < y.data:  # right or left node
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return
        if node.parent.parent is None:  # parent is root
            return
        self.fix_insert(node)

    def left_rotate(self, n):
        y = n.right
        n.right = y.left  # change right child of n to left child of y
        if y.left != self.TNULL:
            y.left.parent = n
        y.parent = n.parent  # parent of y as parent of n
        if n.parent is None:  # root node
            self.root = y
        elif n == n.parent.left:
            n.parent.left = y
        else:
            n.parent.right = y
        y.left = n
        n.parent = y

    def right_rotate(self, n):
        y = n.left  # Y = Left child of n
        n.left = y.right  # Change left child of n to right child of y
        if y.right != self.TNULL:
            y.right.parent = n
        y.parent = n.parent  # Change parent of y as parent of n
        if n.parent is None:
            self.root = y  # Set y as root
        elif n == n.parent.right:
            n.parent.right = y
        else:
            n.parent.left = y
        y.right = n
        n.parent = y

    def fix_insert(self, n):
        while n.parent.color == 1:  # while parent is red
            if n.parent == n.parent.parent.right:  # parent right child
                u = n.parent.parent.left
                if u.color == 1:  # if uncle is red
                    u.color = 0
                    n.parent.color = 0
                    n.parent.parent.color = 1
                    n = n.parent.parent  # repeat with parent node
                else:
                    if n == n.parent.left:  # left child
                        n = n.parent
                        self.right_rotate(n)  # Call for right rotation
                    n.parent.color = 0
                    n.parent.parent.color = 1
                    self.left_rotate(n.parent.parent)

            else:  # if parent is left child of its parent
                u = n.parent.parent.right  # Right child of grandparent
                if u.color == 1:  # uncle node is red
                    u.color = 0  # Set color of children as black
                    n.parent.color = 0
                    n.parent.parent.color = 1  # set color of grandparent as Red
                    n = n.parent.parent  # Repeat algo on grandparent
                else:
                    if n == n.parent.right:  # if n is right child of its parent
                        n = n.parent
                        self.left_rotate(n)  # call left rotate on parent of n
                    n.parent.color = 0
                    n.parent.parent.color = 1
                    self.right_rotate(n.parent.parent)  # call right rotate on grandparent
            if n == self.root:  # If n reaches root then break
                break
            self.root.color = 0 # root always black

    def get_height(self, node):
        if node == self.TNULL:
            return 0
        else:
            l_depth = self.get_height(node.left)
            r_depth = self.get_height(node.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

    def search(self, key):
        root = self.root
        while root != self.TNULL:
            if key > root.data:
                root = root.right
            elif key < root.data:
                root = root.left
            else:
                return True
        return False
