class node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


a = node(1, node(2, node(3, node(4, node(5, node(None))))))


string = ""
while a:
    if a.next == None:
        #print("none")
        string += "None"
    else:
        #print(a.data)
        string += str(a.data) + " "
    a = a.next

print(string.replace(" ", " -> "))
