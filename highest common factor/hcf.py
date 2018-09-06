'''
    euclid's algorithm for two positive integers
    Steps:
        divide p by q to give a remainder r
        if r == 0 then the hcf is q
        otherwise repeat with q and r taking place of p and q prime
'''

#var 1
#note that this variation doesn't work if q = 0
def hcf(p, q):
    r = p % q
    if r == 0:
        return q
    else:
        return hcf(q, r)

#var 2
def hcf2(p,q):
    if q == 0:
        return p
    else:
        return hcf2(q, p%q)

#print(hcf(7,0))
#throws an error


print(hcf(60,45))
#15
print(hcf2(45,60))
#15