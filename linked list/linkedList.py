from node import Node

class MyLinkedList:

    #this is the constructor for the list
    #it has both a head and a tail pointer so the operations are done easier
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #add the specified value to the start of the linked list
    def addAtTheStartOfTheList(self, valueToAdd):
        #first off, create a new node that holds the value you want to be stored
        newNode = Node(valueToAdd)

        #store the value of the head so it doesn't get lost down the road
        temp = self.head

        #now, update the value of the head with the created new node
        #it holds the value you want to store and a pointer to the next value which is null currently
        self.head = newNode

        #update the null pointer with the value of the previous head that is stored
        #in the temp variable
        self.head.nextNode = temp

        #increment the count element
        self.count += 1

        #if there is only one element in the list, the head and tail are the same
        if self.count == 1:
            self.tail = self.head

    def addAtTheEnd(self, valueToAdd):
        #create a node that holds the value to be stored
        newNode = Node(valueToAdd)

        #if the list is empty, it needs to have a value in the head
        #the list cannot start with a null value because it can't iterate over the other elements
        if self.count == 0:
            self.head = newNode
        else:
            #if there is an item in the head, chain the new node to the other nodes
            self.tail.nextNode = newNode
        
        self.tail = newNode
        self.count += 1
        
    def iter(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def size(self):
        return self.count
    