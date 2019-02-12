#a = int(input())

def calc(number):
    start = 1

    def c(s, total):
        if s == number+1:
            return total
        
        total = total + (s * (s+1))
        return c(s+1, total)
    
    res = c(start, 0)

    return res

print(calc(5))

