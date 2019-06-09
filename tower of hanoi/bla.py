
#this function will show how to solve the puzzle taking one piece at a time
#from start to destination with the help of the aux tower
def tower(n, A, B, C):
    if n > 0:
        tower(n-1, A, C, B)
        print("moving from " + str(A) + " to " + str(C))
        tower(n-1, B, A, C)

tower(4, 1,2,3)