import RBTree as RBTree

def main():
    t = RBTree.RBTree()
    t.insert(1)
    t.insert(2)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    t.insert(7)
    t.insert(16)
    t.inorder(t.getRoot())
    print(t.search(5))



main()