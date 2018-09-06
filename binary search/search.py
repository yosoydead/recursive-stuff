'''
    the array MUST be sorted
    we compare the key of the item being sought with the key of the item in the middle of the array
    if it is smaller, then the item, if it is present, must be in the lower half of the array
    else it must be in the upper half
'''

def search(array, itemToSearch):

    def s(low, high):
        if low == high:
            return array[low] == itemToSearch
        else:
            mid = (low+high) //2
            if itemToSearch < array[mid]:
                return s(low, mid)
            else:
                return s(mid+1, high)
    
    return s(0, len(array) -1)

lst = [1,2,3,4,5,29,6,7,8,9]
lst.sort()
print(search(lst, 28))