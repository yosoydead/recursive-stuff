
def rev(n):
    
    #wrapper function
    #i need a way to make the main function return a value
    def r(number,result = 0):
        #if the number has only 1 digit, return that number
        if number < 10:
            return result * 10 + number
        #else, take the result, multiply it with 10 and then add the last digit of the number
        #this way, the first version of result will be the last digit, ex: 1
        #the second call will have result = 1 * 10 + the now last digit whici is 3 => result = 31 
        else:
            result = result * 10 + (number%10)
            return r(number //10, result)

    #call the wrapper function for the result
    return r(n)

print(rev(25461231))