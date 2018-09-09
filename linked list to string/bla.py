class node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

a = node(0, node(1, node(4, node(9, node(16)))))

#main function to convert
def string(node):

    #wrapper function that helps me return the result
    def bla(n = node, result = ""):
        #if the only input is None, the string "None" must be returned
        if n == None:
            return "None"
        
        #if the next node of the current node is None it means that the next node is the end of the list
        #for this, first i need to save the data of the current node, then add the string "None"
        #to the result as well, that being the value of the last item of the list(None)
        #and then, return the result of the entire operation
        if n.next == None:
            #print("none")
            result += str(n.data) + " "
            result += "None"
            return result
        else:
            #if the next node of the current node is not None, save the data of the current node
            #then move down the list
            result += str(n.data) + " "
            return bla(n.next, result)

    #this is the result of the worker function
    finalResult = bla(node)
    #return the string formated as required
    return finalResult.replace(" ", " -> ")

print(string(a))




