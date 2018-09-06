#this solution is my understanding of the problem. if i made a mistake feel free to tell me
def myMax(a, b):
    return a if a > b else b

def myMin(a, b):
    return a if a < b else b

def rng(array):

    def a(index):
        if index == len(array)-1:
            return array[index]
        else:
            return myMax(array[index], a(index+1))
    
    def b(index):
        if index == len(array)-1:
            return array[index]
        else:
            return myMin(array[index], b(index+1))

    return a(0) - b(0)


arr = [1,2,3,9,8,7,4,6,5]
print(rng(arr))