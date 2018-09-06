'''
    this function takes as arguments 3 params: 2 arrays and the length of one of them
    BOTH ARRAYS have to have the same length in order for this to work
    function multiplies the specified indexes from both arrays and then adds them up

    ex: a = [1, 2, 3, 4, 9]
        b = [5, 6, 7, 8, 10]

        index = 0 => return 1 * 5
        index = 1 => return 2*6
        index = 2 => return 3*7
        and so on
'''

def x(a, b, num):
    if num == 0:
        return a[0] * b[0]
    else:
        return x(a,b,num-1) + a[num] * b[num]


a = [1, 2, 3, 4, 9]
b = [5, 6, 7, 8, 10]

print(x(a,b, len(a)-1))
#output 160