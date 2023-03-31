import RBTree as RBTree

t = RBTree.RBTree()
def main(FILENAME):
    i = 0
    with open(FILENAME, 'r') as f:
        for line in f:
            i+=1
            t.insert(line.lower().replace("\n",""))
            print("Inserted: ", line)

    print("Number of words in the dictionary: ", i)
    print("Number of nodes in the tree: ", t.size)

    while(1):
        str = input("Enter a word to insert (-1 to exit):")
        if str == "-1":
            break
        print(" inserted "+ str) if t.insert(str.lower()) else print(" already exists")
        
    
    while(1):
        str = input("Enter a word to search (-1 to exit):")
        if str == "-1":
            break
        print(t.search(str.lower()))


main("EN-US-Dictionary.txt")