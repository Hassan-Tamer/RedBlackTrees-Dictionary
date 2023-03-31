import RBTree as RBTree

def main():
    t = RBTree.RBTree()
    t.insert(1)
    t.insert(2)
    t.insert(3)
    t.inorder(t.getRoot())
    print(t.size)



main()