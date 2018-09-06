'''
    array/list is unordered
    the function goes through the list and compares
    return either true or false
    on average, half of the elements are compared 
    the function runs in O(n)
'''

def search(lst, somethingToSearch):
    
    def s(index):
        #if found return true
        if lst[index] == somethingToSearch:
            return True
        #len(list) -1 because the length function starts counting at 1 even though element indexing starts at 0
        #return false if the index == list length. we compared every single one of the elements in the list
        elif index == len(lst) -1:
            return False
        #increment the index so that the function is not infinite
        else:
            return s(index+1)
    
    return s(0)

lst = [1,2,3,4,5,6,7,8,9]

print(search(lst, 10))
#returns false