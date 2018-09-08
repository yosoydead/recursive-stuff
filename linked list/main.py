from linkedList import MyLinkedList

def main():
    ll = MyLinkedList()
    ll.addAtTheEnd("radu")
    ll.addAtTheEnd("bogdan")
    ll.addAtTheEnd("mircea")
    ll.addAtTheEnd("bla")
    ll.addAtTheEnd("bla")
    ll.addAtTheEnd("another radu")
    print("head", ll.head.data)
    print("tail",ll.tail.data)
    # ll.addAtTheStartOfTheList("radu")
    # ll.addAtTheStartOfTheList("bogdan")
    # ll.addAtTheStartOfTheList("mircea")
    # ll.addAtTheStartOfTheList("bla")
    # print("head", ll.head.data)
    # print("tail",ll.tail.data)
    print("size of the list", ll.size())
    ll.iter()

if __name__ == "__main__":
    main()