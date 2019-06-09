#these are global variables because in python there are no static variables
power = 1
factorial = 1

def e(x, n):
    #as i subtract from n, i need to return 1 when n = 0
    #because 0! = 1
    if n == 0:
        return 1
    else:
        r = e(x, n-1)

        #im using this to calculate the power of x
        #every time the function returns, x will be multiplied by itself so it becomes power of x
        global power
        power = power * x

        #this var is used to calculate the factorial of n
        #every time the function will return, the value of n will be incremented by 1
        global factorial
        factorial = factorial * n

        return r + (power/factorial)

#this function will take common factors from the equation
s = 1
def e2(x,n):
    global s
    if n == 0:
        return s
    else:
        s = 1 + x/n * s

        return e(x,n-1)


print(e2(2,10))