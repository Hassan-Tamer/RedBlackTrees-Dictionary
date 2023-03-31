BLACK = 0
RED = 1


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = RED


class RBTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = BLACK
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.size = 0

    def __min(self, root: Node):
        while root.left != self.NULL:
            root = root.left

        return root.val

    def __leftRotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y
            y.left = x
            x.parent = y

        y.left = x
        x.parent = y

    def __rightRotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __fixInsert(self, k):
        while k.parent.color == 1:  # While parent is red
            if (
                k.parent == k.parent.parent.right
            ):  # if parent is right child of its parent
                u = k.parent.parent.left  # Left child of grandparent
                if (
                    u.color == 1
                ):  # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0  # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # Set grandparent node as Red
                    k = (
                        k.parent.parent
                    )  # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:  # If k is left child of it's parent
                        k = k.parent
                        self.__rightRotate(k)  # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__leftRotate(k.parent.parent)
            else:  # if parent is left child of its parent
                u = k.parent.parent.right  # Right child of grandparent
                if (
                    u.color == 1
                ):  # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0  # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # set color of grandparent as Red
                    k = (
                        k.parent.parent
                    )  # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:  # if k is right child of its parent
                        k = k.parent
                        self.__leftRotate(k)  # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__rightRotate(
                        k.parent.parent
                    )  # Call right rotate on grandparent
            if k == self.root:  # If k reaches root then break
                break
        self.root.color = 0  # Set color of root as black

    def insert(self, key):
        self.size += 1
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = RED

        root = self.root
        parent = None
        while root != self.NULL:
            parent = root
            if key > root.val:
                root = root.right
            elif key < root.val:
                root = root.left

        node.parent = parent
        if parent == None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        if node.parent == None:  # it is the root
            node.color = BLACK
            return

        if node.parent.parent == None:  # the tree consists of 2 levels
            return

        self.__fixInsert(node)

    def inorder(self, begin: Node):
        if begin != self.NULL:
            self.inorder(begin.left)
            print(begin.val)
            self.inorder(begin.right)

    def getRoot(self):
        return self.root

    def search(self, key):
        root = self.root
        while root != self.NULL:
            if key > root.val:
                root = root.right
            elif key < root.val:
                root = root.left
            else:
                return True

        return False
