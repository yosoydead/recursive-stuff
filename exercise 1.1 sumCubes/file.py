'''
    write a function with the heading: 
        SumCubes(n)
    whose values is the sum of the cubes of the integers 1 to n.
    that is: 1^3 + 2^3 + 3^3 .... + n^3
'''

import math

def SumCubes(n):
    if n == 1:
        return 1
    else:
        return math.pow(n,3) + SumCubes(n-1)

print(SumCubes(4))
