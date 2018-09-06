import math
'''
    we can express the condition N is prime as the condition:
    N has no factors between 2 and N^1/2
'''

def prime(n):

    def hasFactors(i):
        if math.pow(i, 2) > n:
            return False
        elif n % 2 == 0:
            return True
        else:
            return hasFactors(i+1)

    return not hasFactors(2)

print(prime(74))