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

    def __fixInsert(self, k:Node):
        while k.parent.color == RED:
            if (k.parent == k.parent.parent.right):
                u = k.parent.parent.left
                if (u.color == 1):
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__rightRotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.__leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if (u.color == RED):
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.__leftRotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.__rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK

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
            else:
                print("Duplicate key")
                return False

        node.parent = parent
        if parent == None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        if node.parent == None:  # it is the root
            node.color = BLACK
            return True

        if node.parent.parent == None:  # the tree consists of 2 levels
            return True

        self.__fixInsert(node)
        return True

    def inorder(self, begin: Node):
        if begin != self.NULL:
            self.inorder(begin.left)
            print(begin.val)
            self.inorder(begin.right)

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
    
    def getRoot(self):
        return self.root

    def getHeight(self,node:Node):
        if(node == self.NULL):
            return 0
 
        else:
          lDepth = self.getHeight(node.left)
          rDepth = self.getHeight(node.right)
 
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1