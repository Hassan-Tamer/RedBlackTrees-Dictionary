import RBT

t = RBT.RedBlackTree()


def search_loop():
    while (1):
        str = input("Enter a word to search (-1 to exit):")
        if str == "-1":
            break
        print(t.search(str.lower()))


def insert_loop():
    while (1):
        str = input("Enter a word to insert (-1 to exit):")
        if str == "-1":
            break
        print(str + " exists") if t.insert_node(str.lower()) == False else print(str + " inserted")
        print("Number of nodes in the tree: ", t.size)
        print("Height of the tree: ", t.get_height(t.root))


def main(filename):
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
            t.insert_node(line.lower().replace("\n", ""))
            # print("Inserted: ", line)
    print("Number of words in the dictionary: ", i)
    print("Number of nodes in the tree: ", t.size)
    print("Height of the tree: ", t.get_height(t.root))

    while (1):
        string = input("Enter a 1 to insert or 2 to search (-1 to exit):")
        if string == "-1":
            break
        if string == "1":
            insert_loop()
        if string == "2":
            search_loop()


main("EN-US-Dictionary.txt")
