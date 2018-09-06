"""
write a function with the header:
    function Max(intArray)
whose value is that of the maximum element of the integer array [0.... n]
"""

def myMax(arr):

    def m(index):
        if index == len(arr) -1:
            return arr[index]
        else:
            return max(arr[index], m(index+1))

    return m(0)
        
array = [1,2,3,9,8,7,4,6,5]
print(myMax(array))


