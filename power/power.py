import math
'''
    single-level function
    number is compared with 0 on every call; if it is different from 0 on the first call
    then it will always be different from 0

    exp is always tested as well; if it were negative initially, its value would have been
    immediately negated
'''
def power(number, exp):
    if number == 0:
        return 0
    elif exp < 0:
        return 1/power(number, -exp)
    elif exp == 0:
        return 1
    else:
        return number * power(number, exp-1)

print(power(2,4))

'''
    two-level function
    this help avoid comparison on every function call
'''

#this is not very efficient for large values of exp
#x^14: this would multiply x by itself 13 times
def power2(number, exp):

    def p(k):
        if k == 0:
            return 1
        else:
            return number * p(k-1)
    
    if number == 0:
        return 0
    elif exp < 0:
        return 1/p(-exp)
    else:
        return p(exp)

print(power2(2,3))


#this runs in O(log n)
#method is called halving and squaring
#x^14: it would square x^7
'''
    0, if x = 0
    1/x^-n, if x != 0 and n< 0
    1, if x != 0, n =0
    x^n/2 * x^n/2 * x, if x != 0 and n is odd
    x^n/2 * x^n/2, x != 0 and n is even 
'''
def power3(number, exp):

    def p2(k):
        if k == 0:
            return 1
        elif k % 2 != 0:
            return math.pow(p2(k //2) , 2) * number
        else:
            return math.pow(p2(k //2) , 2)

    if number == 0:
        return 1
    elif exp < 0:
        return 1/p2(-exp)
    else:
        return p2(exp)

print(power3(2,3))

#the bad solution
#at each level, p is called twice
def power4(number, exp):

    def p3(k):
        if k == 0:
            return 1
        elif k % 2 != 0:
            return p3(k//2) * p3(k//2) *number
        else:
            return p3(k//2)*p3(k//2)
    if number == 0:
        return 1
    elif exp < 0:
        return 1/p3(-exp)
    else:
        return p3(exp)