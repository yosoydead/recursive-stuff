#i chose two random numbers for a and b variables
#a = 2, b = 5
def T(k):
    if k == 0:
        return 2
    return 5 + T(k//2)

print(T(10))

"""
    T(10) returns 22
    Calls:
        k = 10 => return 5 + T(5)
        k = 5 => return 5 + T(2)
        k = 2 => return 5 + T(1)
        k = 1 => return 5 + T(0)
        k = 0 => return 2
    Call stack clear:
        T(0) = 2
        T(1) = 5 + T(0) = 5+2 = 7
        T(2) = 5 + T(1) = 5+7 = 12
        T(5) = 5 + T(2) = 5+12 = 17
        T(10) = 5 + T(5) = 5+17 = 22
"""