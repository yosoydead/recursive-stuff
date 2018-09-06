#n factorial => n!
#ex: 5! = 5*4*3*2*1
#0! = 1
#it is for non-negative integers only
#this is a one level procedure

def fact(number):
    #to make one less calculation this could have been
    #if number == 1: return 1
    if number == 0:
        return 1
    return fact(number-1) * number

print(fact(8))

