#i need n = the number of characters for each combination
#i need i = the starting index. also, i use the index for the list to add the specific combination at each list index
#problem here: in python i can't declare an array of certain length to access and modify certain elements
#   i need to manually create a number of empty entries in the list so i can access them and modify the as needed
#   if i manage to solve this, i will update the solution
n = 3
l = ['', '', '']

def gen(i=0):
    if i == n:
        print(l)
    else:
        l[i] = '*'
        #l[i] = '0'
        gen(i+1)
        l[i] = '-'
        #l[i] = '1'
        gen(i+1)

gen()

''' 
    output sample
    ['*', '*', '*']
    ['*', '*', '-']
    ['*', '-', '*']
    ['*', '-', '-']
    ['-', '*', '*']
    ['-', '*', '-']
    ['-', '-', '*']
    ['-', '-', '-']
'''