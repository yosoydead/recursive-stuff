def initializeArray(n):
    bla = []

    for i in range(0, n):
        bla.append(-1)

    return bla

def fib(n, array):
    #this will initialize indexes at 0 and 1 so both will have the value of 1
    if n<=1:
        array[n] = n
        return n
    else:
        #if i dont know the answer for that value, execute the call to fib(n-2)
        if array[n-2] == -1:
            array[n-2] = fib(n-2, array)
            
        #if i dont know the answer for that value, call fib(n-1)
        if array[n-1] == -1:
            array[n-1] = fib(n-1,array)

    return array[n-2] + array[n-1]
    
x = initializeArray(10)

print(fib(10,x))
print(x)