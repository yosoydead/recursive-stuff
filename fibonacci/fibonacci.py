#iterative function
def fibIter(number):
    a = 0
    b = 1
    c = 0
    for i in range(0, number):
        a=b
        b=c
        #print("i", i, "fib",c)
        c=a+b
    return c   

#recursive function
#it is not efficient because it calls the fib function twice at every execution
def fibRec(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        result = fibRec(number-1) + fibRec(number-2)
        return result

#recursive function with memoization
#we give it a dictinary with the first two numbers of the sequence
#if the value is in dict, simply return the value
#if it isn't, map the current index of the sequence to the state of the function in the dict, then continue the execution. 
#   at one point it will start replacing the state of the function with the value it needs
def memo(number, dic):
    if number in dic:
        return dic[number]
    else:
        ans = memo(number-1, dic)+ memo(number-2,dic)
        dic[number] = ans
        return ans

n = 40
dic = {0:0, 1:1}
memo(n, dic)
print("n is", n)
#fibIter(12)
print("rec",fibRec(n))
#print("iter",fibIter(n))
#print("dic after memo", dic, "and result of", n, "is", dic[n])