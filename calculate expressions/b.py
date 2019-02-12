#a = int(input())

def calc(number):
    const = 1

    def c(s, total):
        if(s == number +1):
            return total
        
        total = total + (const/s)

        return c(s+1, total)

    res = c(1, 0)

    return res

print(calc(5))