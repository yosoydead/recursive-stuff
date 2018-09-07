from node import Node

def printNode(node):
    while node != None:
        print(node.data)
        node = node.nextNode

def main():
    #this is what is happening
    a = Node(1)
    # |1 | null|
    # --- ------
    b = Node(2)
    # |1 | null ----> 2 | null|
    # --- -----      ---  -----  
    c = Node(3)
     # |1 | null ----> 2 | null ----> 3 | null|
    # --- -----      ---  -----      ---  -----

    #print("a")
    a.nextNode = b
    b.nextNode = c

    printNode(a)
    

    # print(b.data)

if __name__ == "__main__":
    main()